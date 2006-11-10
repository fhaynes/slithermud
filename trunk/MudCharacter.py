"""
The MudCharacter class.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import string

import MudObject
import MudWorld
import MudConst
import MudOlc
import MudDatabase
import MudProtocol

class MudCharacterTemplate:
    def __init__(self):
        self.id_num   = 0
        self.name = 'A formless blob'
        self.desc = 'This is a formless blob of protomatter.'
        
        self.commands   = []
        self.logics     = []
        self.statistics = {}
        
class MudCharacter(MudObject.MudObject):
    """
    Class for mobiles and players.
    
    The only difference between the two is that the player has a socket
    reference, whereas with a mobile it is simply an empty string.
    """
    
    def __init__(self, sockRef=''):
        MudObject.MudObject.__init__(self)
        self.sockRef      = sockRef
        
        self.roomRef      = None
        self.zoneRef      = None
        
        self.password     = ''
        self.login_state  = ''
        self.buffer       = ''
        
        self.zone         = 0
        self.room         = 0
        self.admin_level  = 1


        self.items        = {}
        self.ticks_since_last_input = 0
        
    def saveMe(self):
        MudDatabase.db.saveCharToDisk(self)
        
    def writeWithPrompt(self, data):
        try:
            data = MudWorld.world.protocolHandler.processText(data)
            data = MudProtocol.wrapText(data)
            self.sockRef.write('\r\n'+data+'\r\n'+self.prompt())
        except:
            pass
        
    def writePlain(self, data):
        try:
            data = MudWorld.world.protocolHandler.processText(data)

            self.sockRef.write(data)
        except:
            pass
    
    def addItem(self, item):
        self.items[item.id_num] = item
        
    def removeItem(self, item):
        del self.items[item.id_num]
        
    def setRoom(self, room):
        self.room = room
        self.updateRoomRef()
    
    def setZone(self, zone):
        self.zone = zone
        self.updateZoneRef()
        
    # Updates the room reference
    def updateRoomRef(self):
        self.roomRef = MudWorld.world.databaseHandler.returnRoomRef(self.zone, self.room)
 
    # Updates the zone reference
    def updateZoneRef(self):
        self.zoneRef = MudWorld.world.databaseHandler.returnZoneRef(self.zone)

    # Returns a basic prompt.
    def prompt(self):
        return '\r\n'+self.name+'> '


        


