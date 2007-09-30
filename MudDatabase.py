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
        file = open(MudConst.zoneDir+zone.getName()+os.sep+zone.getName()+'.zne', 'wb')
        pickle.dump(zone, file)
        file.close()
        
    def loadZone(self, name):
        """Unpickles a zone file. Takes the zone name as an argument."""
        file = open(MudConst.zoneDir+os.sep+name+'.zne', 'r')
        return pickle.load(file)
    
    def loadPlayer(self, name, player):
        """Attempts to load a player file. NOT FOR NPCS!"""
        file = open(MudConst.playerDir+name+'.ply')
        tmp = pickle.load(file)
        player.info = copy.deepcopy(tmp.info)
        del tmp
        file.close()
    
    def savePlayer(self, player):
        """Pickles a player to a file. NOT FOR NPCS!"""
        file = open(MudConst.playerDir+player.getName()+'.ply', 'wb')
        pickle.dump(player, file)
        file.close()
        
        