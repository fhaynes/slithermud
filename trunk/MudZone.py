"""
MudZone.py
Author: Fletcher Haynes (kurosknight@gmail.com)
Date  : 9/24/07
All Rights Reserved
"""

import MudObject

class MudZone(MudObject.MudObject):

    def __init__(self):
        MudObject.MudObject.__init__(self)
    
        # A dictionary of all rooms in the zone. Key is the ID of the room.
        self.info['rooms']      = {}
    
        # A dictionary of characters. Key is the name of the character.
        self.info['characters'] = {}
        
        # Next max room ID
        self.nextRoomId = 1
        
        # List of free Room IDs
        self.freeRoomIds = []
        
    def addRoom(self, room):
        """
        Adds a room to the dictionary. Takes a room instance as the argument,
        and it uses the ID Number of the room instance as the key.
        """
        self.info['rooms'][room.info['id_num']] = room
        room.setZone(self)
        
    def remRoom(self, room_id):
        """
        Deletes a room from the zone object. Takes the ID of the room to
        delete from the dictionary.
        """        
        del self.info['rooms'][room_id]
        
    def getRoom(self, room_id):
        """
        Returns a room instance with a matching id_num.
        """
        return self.info['rooms'][room_id]
    
    def getRooms(self):
        """Returns the rooms dictionary."""
        return self.info['rooms']
        
    def addCharacter(self, character):
        """
        Adds a character to the dictionary. Uses the name of the character
        as a key.
        """
        self.info['characters'][character.info['name']] = character
        character.setZoneRef(self)
        
    def removeCharacter(self, character_name):
        """
        Removes a character instance from the zone object.
        """
        del self.info['characters'][character_name]
    
    def getCharacter(self, character_name):
        """
        Returns a character instance with a matching name.
        """
        return self.info['characters'][character_name]
    
    # ------------------------------------ #
    # Functions for assigning IDs to Rooms #
    # and for handling recycling old ones  #
    # ------------------------------------ #
    
    def addFreeId(self, idNum):
        """This takes an ID number and adds it to freed room list."""
        self.freeItemTemplateIds.append(int(idNum))
        self.freeItemTemplateIds.sort(reverse=True)
        
    def getNewId(self):
        """Returns the next free Room ID number for the zone."""
        try:
            return self.freeRoomIds.pop()
        except IndexError:
            nextId = self.nextRoomId
            self.nextRoomId += 1
            return nextId
        
    
    