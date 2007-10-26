"""
New and improved core network server for Slither.
It handles server-type stuff, like connections, disconnects
and most importantly, player input. :)

@author: Fletcher Haynes/Adam "Vopisk" Dean
@copyright: (c)2007 Fletcher Haynes/Adam Dean, All Rights Reserved.
"""

import twisted.protocols.basic

import MudCharacter
import MudProtocol
import InputHandler
import MudConst
import logger

class MudServer(twisted.protocols.basic.LineOnlyReceiver):
    """
    This is the custom protocol class for the MUD Server.
    Updated this to be a twisted basic.LineOnlyReceiver
    for speed enhancements sake.
    """
    def __init__(self):
        self.delimiter = '\n'

    def connectionMade(self):
        """
        Handles incoming connections.

        For right now, we'll stick to how we've been doing it, because it works.
        Creates a new instance of the Character class and asks for an account name.
        Provides the tansport layer to the class for I/O.
        """
        logger.logging.info('New connection from %s' % str(self.transport.getPeer()))
        self.playerRef = MudCharacter.MudCharacter(self.transport)
        self.playerRef.info['login_state'] = MudConst.getAccountName
        self.transport.write(MudProtocol.protocolHandler.processText(MudConst.greeting))
        self.transport.write('\r\nEnter account name, or "new" to create a new character: ')

    def connectionLost(self, reason):
        """
        Handles dropped connections.
        """
        pass

    def lineReceived(self, line):
        """
        Passes all input from the connection through the InputHandler.
        """
        line = line.strip('\r\n')
        InputHandler.handler.handleInput(self.playerRef, line)