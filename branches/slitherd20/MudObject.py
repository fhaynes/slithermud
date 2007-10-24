"""
MudObject.py
Author: Fletcher Haynes (kurosknight@gmail.com)
Date  : 9/24/07
All Rights Reserved
"""

class MudObject:
    """
    Base class for all objects in the MUD.
    """

    def __init__(self):
        # Base dictionary and sub-dictionaries
        self.info           = {}
        self.info['statistics']     = {}
        self.info['commands']       = {}
        self.info['logics']         = {}
        self.info['hooks']          = []
        
        # Name of the object, description, and ID Number. All Objects in the
        # MUD will have these.
        self.info['name']   = 'A Blank Name'
        self.info['desc']   = 'A blank description.'
        self.info['id_num'] = 0
    
    # ---------------------- #    
    # Get and Set functions  #
    # ---------------------- #
    def setName(self, newName):
        '''
        Sets the name of the object.
        '''
        self.info['name'] = newName
        
    def getName(self):
        '''
        Returns the name of the object.
        '''
        return self.info['name']
    
    def setDesc(self, newDesc):
        '''
        Sets the description of the object.
        '''
        self.info['desc'] = newDesc
        
    def getDesc(self):
        '''
        Returns the description of the object.
        '''
        return self.info['desc']
        
    def setId(self, newId):
        '''
        Sets the new ID of the object. Numbers only.
        '''
        self.info['id_num'] = newId
        
    def getId(self):
        '''
        Returns the ID of the object.
        '''
        return self.info['id_num']
    
    def addStat(self, statName, statValue):
        # TODO: Should we throw an exception if the stat already exists?
        # Or should we combine addStat and setStat into one function?
        # Right now, both do the same thing.
        """Adds a stat to the dictionary."""
        self.info['statistics'][statName] = statValue
        
    def removeStat(self, statName):
        '''Deletes a stat from the dictionary.'''
        del self.info['stats'][statName]
        
    def setStat(self, statName, statValue):
        '''
        Sets a statistic in the statistics dictionary.
        '''
        self.info['stats'][statName] = statValue
        
    def getStat(self, statName):
        '''
        Returns the value of a requested statistic.
        '''
        return self.info['stats'][statName]
    
    def hasStat(self, statName):
        '''
        Checks if the object has a stat in the info dictionary.
        '''
        if self.info['stats'].has_key(statName):
            return True
        else:
            return False
        
    def getStats(self):
        """Returns the entire stat dictionary."""
        return self.info['stats']
        
    def addCommand(self, newCmd, cmdInst):
        '''
        Adds a command to the dictionary.
        '''
        self.info['commands'][newCmd] = cmdInst
        
    def removeCommand(self, command):
        '''
        Removes a command from the dictionary.
        '''
        del self.info['commands'][command]

    def getCommands(self):
        '''
        Returns a list of all the command names
        '''
        return self.info['commands'].keys()                 
        
    def addLogic(self, newLogic, logicInst):
        '''
        Adds a logic module to the dictionary.
        '''
        self.info['logics'][newLogic] = logicInst
        
    def removeLogic(self, moduleName):
        '''
        Removes a logic module from the dictionary.
        '''
        del self.info['logics'][moduleName]
        
    def getLogic(self, moduleName):
        """Returns the specified logic module."""
        return self.info['logics'][moduleName]
    
    def getLogics(self):
        """Returns the logics list."""
        return self.info['logics']
        
    def addHook(self, action):
        """
        Adds a reference (or hook) to the supplied Action.
        """
        self.info['hooks'].append(action)
        
    def removeHook(self, action):
        """
        Deletes a reference (or hook) to the supplied Action.
        """
        del self.info['hooks'][action]
        
    def clearHooks(self):
        """
        Clears all the hooks to all actions.
        """
        for eachHook in self.info['hooks']:
            eachHook.setValid(False)
            del eachHook
            
    def getInfo(self):
        """
        Returns a reference to the entire info dictionary.
        """
        return self.info

        
    # ------------------------- #    
    # Action related functions  #
    # ------------------------- #
        
    def doQuery(self, action):
        """
        Sends an Action instance to each logic module attached to this
        entity. It then returns the result of each.
        """
        for eachLogic in self.info['logics'].values():
            result = eachLogic.process(action, self)
            if result == 1:
                return 1
        return 0
    
    def doAction(self, action):
        """Sends an action to all the modules with no returning of values."""
        for eachLogic in self.info['logics'].values():
            eachLogic.process(action, self)
        