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
    