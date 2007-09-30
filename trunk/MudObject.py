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
        
        # Name of the object, description, and ID Number. All Objects in the
        # MUD will have these.
        self.info['name']   = ''
        self.info['desc']   = ''
        self.info['id_num'] = 0
    
    # ---------------------- #    
    # Get and Set functions
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
        
    def setStat(self, statName, statValue):
        '''
        Sets a statistic in the statistics dictionary.
        '''
        self.info['statistics'][statName] = statValue
        
    def getStat(self, statName):
        '''
        Returns the value of a requested statistic.
        '''
        return self.info['statistics'][statName]
        
    def addCommand(self, newCmd, cmdInst):
        '''
        Adds a command to the dictionary.
        '''
        self.info['commands'][newCmd] = cmdInst
        
    def remCommand(self, command):
        '''
        Removes a command from the dictionary.
        '''
        del self.info['commands'][command]
        
    def addLogic(self, newLogic, logicInst):
        '''
        Adds a logic module to the dictionary.
        '''
        self.info['logics'][newLogic] = logicInst
        
    def remLogic(self, module_name):
        '''
        Removes a logic module from the dictionary.
        '''
        del self.info['logics'][module_name]

        
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
        