"""
This is the standard command class for the MUD. All commands are derived
from this.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import sys

import MudActionHandler
import MudAction
class MudCommand:
    """
    Class for each command in the MUD.
    
    A reference to the instance of this class is attached to any Object that
    can use the command. It creates the appropiate instance of an Action
    object and passes it to the ActionHandler.
    """
    
    def __init__(self):
        self.cmdName = ''
        self.helpText = ''
        self.useExample = ''