"""
MudItem.py
Author: Fletcher Haynes (kurosknight@gmail.com)
Date  : 9/24/07
All Rights Reserved
"""

import MudObject

class MudItem(MudObject.MudObject):
    """
    This class represents items in the game. A sword, gold coins, and such.
    """
    def __init__(self):
        MudObject.MudObject.__init__(self)
        # Player that owns the item. Is a reference to the character instance.
        self.info['owner']      = None
        
        # Reference to the instance of the room the item is in.
        self.info['roomRef']       = None
        
        # Wether or not the item is a quantity item.
        # Coins vs a sword, for example
        self.info['isQuantity'] = False
        
        # If it is a quantity item, how many are there?
        self.info['quantity']   = 1
        
    def setOwner(self, newOwner):
        """Sets the reference to the owner of the item."""
        self.info['owner'] = newOwner
        
    def getOwner(self):
        """Returns reference to owner of the item."""
        return self.info['owner']
        
    def setRoomRef(self, newRoom):
        """Sets the reference to the room the item is in."""
        self.info['roomRef'] = newRoom
        
    def getRoomRef(self):
        """Returns the reference to the room the item is in."""
        return self.info['roomRef']
        
    def getQuantity(self):
        """Returns the quantity of the item."""
        return self.info['quantity']
        
    def setQuantity(self, quantity):
        """Sets the quantity of the item."""
        self.info['quantity'] = quantity
        
    def setIsQuantity(self, flag):
        """Set wether or not the item is a quantity item."""
        self.info['isQuantity'] = flag
        
    def getIsQuantity(self):
        """Returns if the item is a quantity item or not."""
        return self.info['isQuantity']
        