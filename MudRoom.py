"""
MudRoom.py

Contains the class for a room in the MUD.
Author: Fletcher Haynes (kurosknight@gmail.com)
Copywrite 2007, All Rights Reserved
"""

import MudObject

class MudRoom(MudObject.MudObject):
    def __init__(self):
        MudObject.MudObject.__init__(self)
        
        self.info['zone']       = {}
        
        self.info['portals']    = {}
        self.info['items']      = {}
        self.info['characters'] = {}

    def addItem(self, item):
        self.info['items'][item.info['id_num']] = item
        
    def removeItem(self, item):
        del self.info['items'][item.info['id_num']]
        
    def addCharacter(self, character):
        """
        Adds a Character to the room dictionary.
        
        Keys are Character names, value is a reference to the Character instance.
        """
        self.info['characters'][character.info['name']] = character
        character.setRoomRef(self)

    def removeCharacter(self, character):
        """
        Removes a character from the room.
        """
        del self.info['characters'][character.info['name']]

    def addPortal(self, portal):
        """
        Adds a portal to the room.
        """
        self.info['portals'][portal.info['id_num']] = portal
        portal.setRoomRef(self)

    def removePortal(self, portal):
        """
        Removes a portal from the room.
        """
        del self.info['portals'][portal.info['id_num']]
        
    def getPortals(self):
        """Returns the portal dictionary."""
        return self.info['portals']
    
    def getCharacters(self):
        """Returns the character dictionary."""
        return self.info['characters']
    
    def getItems(self):
        """Returns the items dictionary."""
        return self.info['items']
    
    def findItemByName(self, name):
        "Searchs for an item by name."""
        for eachItem in self.getItems().values():
            if eachItem.getName().lower() == name.lower():
                return eachItem
        return None
    
    def setZone(self, zone):
        self.info['zone'] = zone