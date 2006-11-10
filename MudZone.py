"""
Contains the MudZone class definition.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import MudCharacter
import MudObject
import MudRoom


class MudZone(MudObject.MudObject):
    """
    Class for zones in the MUD.
    
    Contains the following:
    - Dictionary for characters in the zone, with ID num as the key.
    - A dictionary of rooms in the zone, with ID num as the key.
    - A list of players allowed to edit this zone.
    """
    def __init__(self):
        MudObject.MudObject.__init__(self)
        
        # Rooms are indexed by id number. Shocking, isn't it?
        self.rooms      = {}
        
        self.characters = {}
        
        # OLC Stuff
        # List of names who are allowed to edit this zone
        self.allowed    = []
        
        self.next_room_id = 2
        self.next_portal_id = 1
        
        for eachRoom in self.rooms.values():
            self.next_room_id = eachRoom.id_num + 1

        for eachRoom in self.rooms.values():
            for eachPortal in eachRoom.portals.values():
                self.next_portal_id = eachPortal.id_num + 1
        
                
    def addRoom(self, room):
        """
        Adds a room to the zone, with ID num as the key.
        """
        self.rooms[room.id_num] = room

    def removeRoom(self, room):
        """
        Removes a room from the dictionary, with ID num as the key.
        """
        del self.rooms[room.id_num]
        
    def addCharacter(self, character):
        self.characters[character.id_num] = character
        
    def removeCharacter(self, character):
        del self.characters[character.id_num]
            
    def returnCharacters(self):
        m_list = []
        for eachCharacter in self.characters.values():
            m_list.append(eachCharacter)
        return m_list
    
    def generateNextPortalId(self):
        id_num = self.next_portal_id
        self.next_portal_id = self.next_portal_id + 1
        return id_num 
    
    def generateNextRoomId(self):
        id_num = self.next_room_id
        self.next_room_id = self.next_room_id + 1
        return id_num 