"""
This class is anything a MudObject can do. Anytime they move, look, or
anything else, one of these is generated and then passed around to any logic
files associated with what they are trying to do.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

class MudAction:
    """
    Class for any action that takes place in the MUD.
    
    Commands create an instance of the MudAction class and pass it to the
    appropiate logic modules attached to all objects.
    """
    def __init__(self):
        self.actionType    = ''
        self.playerRef     = ''
        self.data1         = ''
        self.data2         = ''
        self.data3         = ''
        self.string        = ''