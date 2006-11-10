"""
This is our room class. You really should be picking up on the naming pattern
by now, I would think.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""


import MudPortal
import MudObject
import MudRoom

class MudRoom(MudObject.MudObject):
    """
    Class for all rooms in the MUD.
    
    It contains the dictionaries for:
    - All portals, with the ID as a key and a reference to the portal instance
      as the value.
    - All items in the room with the ID as a key and a reference to the item
      instance as the value.
    - All Characters in the room with name as a key and a reference to the
      character as the value.
    """
    def __init__(self):
        MudObject.MudObject.__init__(self)
        self.zone       = 0
     
        # What portals are in the room.
        self.portals    = {}

        # What items are in the room.
        self.items      = {}
        self.characters = {}
        
        self.name = 'White Space'
        self.desc = 'You are surrounded by the formless mists of eternity.'
        
    def addItem(self, item):
        self.items[item.id_num] = item
        
    def removeItem(self, item):
        del self.items[item.id_num]
        
    def findItem(self, name):
        tmp = []
        for eachItem in self.items.values():
            if name.lower() in eachItem.name.lower():
                tmp.append(eachItem)
        return tmp
        
    def addCharacter(self, character):
        """
        Adds a Character to the room dictionary.
        
        Keys are Character names, value is a reference to the Character instance.
        """
        self.characters[character.id_num] = character

    def removeCharacter(self, character):
        """
        Removes a character from the room.
        """
        del self.characters[character.id_num]

    def addPortal(self, portal):
        """
        Adds a portal to the room.
        """
        self.portals[portal.id_num] = portal

    def removePortal(self, portal):
        """
        Removes a portal from the room.
        """
        if self.portals.has_key(portal.id_num):
            del self.portals[portal.id_num]
        else:
            return "Portal does not exist."

    def returnPortals(self):
        """
        Returns a list of portal instances currently in the room.
        """
        p_list = []
        for eachPortal in self.portals.values():
            p_list.append(eachPortal)
        return p_list
    
    def findPortal(self, portal_id):
        return self.portals[int(portal_id)]
    
    def findPortalByName(self, portal_name):
        for eachPortal in self.portals.values():
            if eachPortal.name.lower() == portal_name.lower():
                return eachPortal
        return 0
        
    
            