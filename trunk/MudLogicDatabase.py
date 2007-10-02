"""
MudLogicDatabase.py
Author: Fletcher Haynes
Copyright 2007, All Rights Reserved

This file contains the database that stores all the logic modules in the game.
"""
import copy

import MudConst

class LogicModuleDatabase:
    def __init__(self):
        self.logics = {}
        
    def loadLogic(self, name):
        """Attempts to load a logic module from a file."""
        self.logics[name] = __import__(name)
        
    def loadAllLogics(self):
        """
        Loads all the logic modules listed in logicIndex.txt.
        """
        logicIndex = open(MudConst.logicIndex, 'r')
        for eachLine in logicIndex.readlines():
            eachLine = eachLine.replace("\n", "")
            eachLine = eachLine.replace("\r", "")
            self.loadLogic(eachLine)
        logicIndex.close()
        
    def getLogic(self, name):
        """Returns a copy of a logic module."""
        return name, copy.deepcopy(self.logics[name])