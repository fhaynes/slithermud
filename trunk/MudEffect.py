"""
Holds the MudEffect class.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""


class MudEffect:
    """
    Class for different effects that can be applied to an Object.
    
    When Actions are passed to something with a logic module, the module
    will process it through each Effect to see if it needs to alter that action.
    """
    def __init__(self):
        
        # Reference to the person the Effect is attached too
        self.owner = ''
        
    def Process(self, action):
        """
        Modifies the Action based on what you want the Effect to do.
        """
        pass