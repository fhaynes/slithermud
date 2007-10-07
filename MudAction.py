class MudAction:
    """
    Contains all of the information about attempted physical actions within
    the world. Whenever a Mob, Item, Character, etc tries to do anything in 
    the game world, an instance is created and sent around to all the other
    chars, items, room, etc.
    """

    def __init__(self, actionType, playerRef, data1='', \
                  data2='', data3='', string=''):
        self.info = {}
        self.info['actionType']    = actionType
        self.info['playerRef']     = playerRef
        self.info['data1']         = data1
        self.info['data2']         = data2
        self.info['data3']         = data3
        self.info['string']        = string
        
    def setType(self, type):
        """Sets the action type to the provided string."""
        self.info['actionType'] = type
        
    def setData1(self, data):
        """Sets the Data1 field of the action."""
        self.info['data1'] = data
        
    def setData2(self, data):
        """Sets the Data2 field of the action."""
        self.info['data2'] = data
        
    def setData3(self, data):
        """Sets the Data3 field of the action."""
        self.info['data3'] = data
    
    def setString(self, data):
        """Sets the string field of the action."""
        # TODO: Probably not neccessary to call this string. Holdover from
        # the translated C++ code.
        
        self.string = data
        
    def getType(self):
        """Returns the type of action."""
        return self.info['actionType']
        
    def getPlayerRef(self):
        """Returns a reference to the player who generated the action."""
        return self.info['playerRef']
    
    def getString(self):
        """Returns the String value of the action."""
        return self.info['string']
    
    def getData1(self):
        """Returns the data1 field."""
        return self.info['data1']
    
    def getData2(self):
        """Returns the data2 field."""
        return self.info['data2']
    
    def getData3(self):
        """Returns the data3 field."""
        return self.info['data3']
    

class TimedAction(MudAction):
    def __init__(self, actionType, playerRef, data1='', \
                  data2='', data3='', string=''):
        MudAction.__init__(self, actionType, playerRef, data1='', \
                  data2='', data3='', string='')
        self.executionTime = None
        self.actionEvent   = None
        self.valid         = True
        
    def getExecutionTime(self):
        """
        Returns the time (in miliseconds after start of MUD) that the 
        action should be executed.
        """
        return self.executionTime
    
    def setExecutionTime(self, time):
        """
        Sets the time (in milliseconds after the MUD has started) that the 
        action should be executed.
        """
        self.executionTime = time
        
    def hook(self):
        """
        This hooks a timed action to all it's references.
        """
        
        # TODO: Some error checking code in case the instance/hook no longer
        # exists? Same for unhook...
        if type(self.getPlayerRef()) == 'instance':
            self.getPlayerRef().addHook(self)
        if type(self.getData1()) == 'instance':
            self.getData1().addHook(self)
        if type(self.getData2()) == 'instance':
            self.getData1().addHook(self)
        if type(self.getData3()) == 'instance':
            self.getData1().addHook(self)
            
    def unhook(self):
        """
        This removes a timed action from all it's references.
        """
        if type(self.getPlayerRef()) == 'instance':
            self.getPlayerRef().removeHook(self)
        if type(self.getData1()) == 'instance':
            self.getData1().removeHook(self)
        if type(self.getData2()) == 'instance':
            self.getData1().removeHook(self)
        if type(self.getData3()) == 'instance':
            self.getData1().removeHook(self)
            
    def setValid(self, value):
        """
        Sets the validity of the action.
        """
        if value == True:
            self.valid = True
        elif value == False:
            self.valid = False
        else:
            #TODO: Code to notify that it is an invalid value?
            return
        
        
        

        