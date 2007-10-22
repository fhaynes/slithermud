"""
MudLogicDatabase.py
Author: Fletcher Haynes
Copyright 2007, All Rights Reserved

This file contains the database that stores all the logic modules in the game.
"""
import copy

import MudConst

# Logic Modules 
# Contains the processing classes

import genericRoom
import genericItem
import genericPortal
import genericPlayer

class LogicModuleDatabase:
    def __init__(self):
        self.logics = {}
        self.logics['genericRoom'] = genericRoom.genericRoom
        self.logics['genericItem'] = genericItem.genericItem
        self.logics['genericPlayer'] = genericPlayer.genericPlayer
        self.logics['genericPortal'] = genericPortal.genericPortal
        
    def getLogic(self, name):
        """Returns a copy of a logic module."""
        return name, self.logics[name]()