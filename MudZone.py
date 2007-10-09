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
        
        # Next max portal ID
        self.nextPortalId = 1
        
        # List of free Room IDs
        self.freeRoomIds = []
        self.freePortalIds = []
        
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
        
    def getRoom(self, roomId):
        """
        Returns a room instance with a matching ID.
        """
        return self.info['rooms'][roomId]
    
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
        
    def removeCharacter(self, characterName):
        """
        Removes a character instance from the zone object.
        """
        del self.info['characters'][characterName]
    
    def getCharacter(self, characterName):
        """
        Returns a character instance with a matching name.
        """
        return self.info['characters'][characterName]
    
    # ------------------------------------ #
    # Functions for assigning IDs to Rooms #
    # and for handling recycling old ones  #
    # ------------------------------------ #
    
    def addFreeId(self, idType, idNum):
        """This takes an ID number and adds it to appropiate freed list."""
        if idType == 'room':
            self.freeRoomIds.append(int(idNum))
            self.freeRoomIds.sort(reverse=True)
        elif idType == 'portal':
            self.freePortalIds.append(int(idNum))
            self.freePortalIds.sort(reverse=True)
        else:
            return
        
    def getNewId(self, idType):
        """Returns the next free Room ID number for the zone."""
        
        if idType == 'room':
            try:
                return self.freeRoomIds.pop()
            except IndexError:
                nextId = self.nextRoomId
                self.nextRoomId += 1
                return nextId
        elif idType == 'portal':
            try:
                return self.freePortalIds.pop()
            except IndexError:
                nextId = self.nextPortalId
                self.nextPortalId += 1
                return nextId
        else:
            return
        
    
    