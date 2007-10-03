"""
MudDatabase.py
This object handles all the saving, loading, and searching of characters,
items, rooms, zones, and portals.

Author: Fletcher Haynes (kurosknight@gmail.com)
Copywrite: 2007, All Rights Reserved
"""

import MudConst
import MudWorld
import os
import copy
import cPickle as pickle

class MudDatabase:
    def __init__(self):
        self.players = {}
        

    def saveZone(self, zone):
        """
        Pickles a zone to file using the zone name. 
        Takes a zone instance as the argument.
        """
        zCopy = copy.deepcopy(zone)
        zCopy.info['characters'] = {}
        
        for eachRoom in zCopy.info['rooms'].values():
            eachRoom.info['characters'] = {}

        file = open(MudConst.zoneDir+zCopy.getName()+'.zne', 'wb')
        pickle.dump(zCopy, file)
        file.close()
        del zCopy
        
    def loadZone(self, name):
        """Unpickles a zone file. Takes the zone name as an argument."""
        file = open(MudConst.zoneDir+os.sep+name+'.zne', 'r')
##        x = pickle.load(file)
##        name, genRoom = MudWorld.world.logicDb.getLogic('genericRoom')
##        for eachRoom in x.info['rooms'].values():
##            eachRoom.addLogic(name, genRoom)
##            for eachItem in eachRoom.info['items'].values():
##                iName, genItem = MudWorld.world.logicDb.getLogic('genericItem')
##                eachItem.setRoomRef(eachRoom)
##                eachItem.addLogic(iName, genItem)
##        self.saveZone(x)
##        return x
        return pickle.load(file)
    
    def loadPlayer(self, name, player):
        """Attempts to load a player file. NOT FOR NPCS!"""
        file = open(MudConst.playerDir+name+'.ply')
        tmp = pickle.load(file)
        player.info = copy.deepcopy(tmp.info)

        # Now we need to translate this ID Number back into a instance reference
        # TODO: This will need to take into account unloaded zones when we
        # implement lazy loading. i.e., we will need to check to make sure the
        # zone exists. If not, we can put them somewhere else or load it up.
        
        zoneId = player.getZoneRef()
        roomId = player.getZoneRef()

        player.setZoneRef(MudWorld.world.getZone(zoneId))
        player.setRoomRef(player.getZoneRef().getRoom(roomId))

        del tmp
        file.close()
    
    def savePlayer(self, player):
        """Pickles a player to a file. NOT FOR NPCS!"""
        
        # First we make a copy of the player's data that we will save. We will
        # be changing some things in the player class to make it able to be
        # pickled. We don't want to save actual references to the zones/rooms
        # they are in, so they will need to be translated into integers.
        # Upon loading, we will translate those back into references.
        pCopy = copy.deepcopy(player)

        # We cannot pickle a socket, so we delete that
        pCopy.sockRef = None
        
        zoneId = player.getZoneRef().getId()
        roomId = player.getRoomRef().getId()
        pCopy.setZoneRef(zoneId)
        pCopy.setRoomRef(roomId)

        # We use binary mode since string representations have problems with
        # line endings across different platforms.
        file = open(MudConst.playerDir+player.getName()+'.ply', 'wb')
        pickle.dump(pCopy, file)
        
        # The copy has been saved, so we can safely delete it now.
        del pCopy
        
        file.close()
        
    def saveIdDatabase(self):
        """Saves the ID Database."""
        file = open(MudConst.idDatabasePath, 'wb')
        pickle.dump(MudWorld.world.idDb, file)
        file.close()
        
    def loadIdDatabase(self):
        """Loads the ID Database."""
        file = open(MudConst.idDatabasePath)
        return pickle.load(file)
    
    def saveTemplateDatabase(self):
        """Saves the Template Database."""
        file = open(MudConst.templateDatabasePath, 'wb')
        pickle.dump(MudWorld.world.templateDb, file)
        file.close()
        
    def loadTemplateDatabase(self):
        """Loads the Template Database."""
        file = open(MudConst.templateDatabasePath)
        return pickle.load(file)
        
        