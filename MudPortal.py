"""
This is the Portal class for the MUD. What is a Portal, you ask? I'm glad
you did! A portal is a MudObject that allows movement. Rooms do not have
exits, as such. All room to room movement is handled via portals. You can
have a portal named "north", "south", "Door", etc.Portals can also have
logic scripts, that allows you to do many neat things. You can bar access
to certain races, alignments, if a player has or doesn't have a particular
object, etc etc.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import MudObject

class MudPortal(MudObject.MudObject):
    """
    Class for portals in the MUD
    
    A Portal is an Object that can move a player or mobile from one place to
    another. They can be named anything, such as north for typical directions
    or Door for more specialized directions. Has an anchor attribute to know
    what room it is located in.
    """
    def __init__(self):
        MudObject.MudObject.__init__(self)
        self.anchor      = 0
        self.zone        = 0
        
        self.target_room = 0
        self.target_zone = 0