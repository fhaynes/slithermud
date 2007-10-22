"""
MudPortal.py
Author: Fletcher Haynes (kurosknight@gmail.com)
Date  : 9/24/07
All Rights Reserved
"""

import MudObject

class MudPortal(MudObject.MudObject):
    """
    The Portal class. It contains a dictionary of exits and the corresponding
    information for them (target zone, room, description)
    """
    
    def __init__(self, name, t_room, t_zone):
        MudObject.MudObject.__init__(self)
        self.info['room'] = None
        self.info['name']   = name
        self.info['target_zone'] = t_zone
        self.info['target_room'] = t_room
        
    def setRoomRef(self, room):
        """Sets the reference to the room that owns the portal."""
        self.info['room'] = room
        
    def getTargetZone(self):
        """Returns the target zone ID."""
        return self.info['target_zone']
    
    def getTargetRoom(self):
        """Returns the target room ID."""
        return self.info['target_room']
    