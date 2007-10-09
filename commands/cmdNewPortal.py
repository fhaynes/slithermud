"""
cmdNewPortal.py
Author: Fletcher Haynes
This commands handle adding a portal to a room.
"""

import MudCommand
import MudWorld

import string

class cmdNewPortal(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "newportal"
        self.info['helpText']   = '''Creates a new room with the specified target room and name.'''
        self.info['useExample'] = '''newportal 3 Door of Death'''
        
    def process(self, player, args=''):
        # Let's first get the zone and room the player is in
        z = player.getZoneRef()
        r = player.getRoomRef()
        
        # Let's check the args, to make sure we have all the needed info.
        argList = args.split(" ", 1)
        if len(argList) != 2:
            player.writeWithPrompt("The proper format is newportal ID Name of Portal.")
            return
        
        # Create a new portal with the appropiate values
        newPortal = MudPortal.MudPortal(argList[1], int(argList[0]), z.getId())
        
        # Assign it a unique ID...
        newPortal.setId(z.getNewId('portal'))
        
        # And add it to the room...
        r.addPortal(newPortal)
        
        # Last, save the zone
        MudWorld.world.db.saveZone(z)
        
        player.writeWithPrompt("Portal created!")
        
