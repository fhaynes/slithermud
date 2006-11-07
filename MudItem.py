"""
Holds the MudItem class.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import MudObject

class MudItemTemplate:
    def __init__(self):
        self.id_num   = 0
        self.name = 'A formless blob'
        self.desc = 'This is a formless blob of protomatter.'
        self.logics     = []
        self.statistics = {}
        
    
class MudItem(MudObject.MudObject):
    """
    Item class for the MUD.
    
    Keeps track of who owns it, and what it contains, if anything.
    """
    def __init__(self):
        MudObject.MudObject.__init__(self)
        
        # This is if the item is a container object, like a bag or something. It
        # is a list of everything in the item
        self.contains   = []
        
        # Who owns the item
        self.owner      = None
        self.room       = None
        self.zone       = None
        self.isQuantity = False
        self.quantity   = 1
        
    def setQuantity(self, q):
        self.quantity = int(q)
        