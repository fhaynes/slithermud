"""
This is the core network server. It handles connections, disconnected, etc.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import string

import twisted.protocols.basic

import MudCharacter
import MudProtocol
import MudWorld
import MudConst
import MudDatabase

class MudServer(twisted.protocols.basic.LineReceiver):
    """
    Custom class for the MUD Server.
    """
    def __init__(self):
        self.delimiter = '\n'
        
    def connectionMade(self):
        """
        Handles incoming connections.
        
        Creates a new instance of the Character class and asks for an account
        name. Provides the transport layer to the class for I/O.
        """
        print "New Connection!"
        self.playerRef = MudCharacter.MudCharacter(self.transport)
        self.playerRef.login_state = MudConst.getAccountName
        self.transport.write(MudProtocol.protocolHandler.processText(MudConst.greeting))
        self.transport.write('\r\nEnter account name, or "new": ')

    def connectionLost(self, reason):
        """
        Handles dropped connections.
        """
        if self.playerRef.zoneRef != None:
            self.playerRef.zoneRef.removeCharacter(self.playerRef)
            self.playerRef.roomRef.removeCharacter(self.playerRef)
            MudDatabase.db.removeCharacter(self.playerRef)
            try:
                MudDatabase.db.cleanUpCharItems(self.playerRef)
            except:
                pass
    def lineReceived(self, line):
        """
        Calls the input handler of the Character class.
        """
        line = line.replace('\r', '\n', 1)
        line = line.strip('\r')
        line = line.strip('\n')
        MudWorld.world.handleInput(self.playerRef, line)        
            
        