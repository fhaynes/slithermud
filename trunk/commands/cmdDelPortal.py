"""
cmdDelPortal.py
Author: Fletcher Haynes
This commands handle deleting a portal from a room.
"""

import MudCommand
import MudWorld

import string

class cmdDelPortal(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "delportal"
        self.info['helpText']   = '''Deletes a portal from the room, based on supplied ID.'''
        self.info['useExample'] = '''delportal 3'''
        
    def process(self, player, args=''):
        if not args.isdigit():
            player.writeWithPrompt("You must supply an ID to the portal to delete.!")
            return
        
        r = player.getRoomRef()
        z = player.getZoneRef()
        try:
            r.removePortal(int(args))
            z.addFreeId('portal', int(args))
        except KeyError:
            player.writeWithPrompt("Could not find that portal.")
            return
            
        
        
