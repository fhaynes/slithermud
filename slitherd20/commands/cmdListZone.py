"""
cmdListZone.py
Author: Fletcher Haynes
This command handles listing all zone names and IDs, or info about one zone.
"""

import MudCommand
import MudWorld

import string
import os

class cmdListZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "listzone"
        self.info['helpText']   = '''Lists all zone names and IDs, or more specific info about a specified zone.'''
        self.info['useExample'] = '''listzone (zoneid)'''
        
    def process(self, player, args=''):
        if args == '':
            player.writePlain('\r\n')
            for eachZone in MudWorld.world.getZones().values():
                player.writePlain('['+str(eachZone.getId())+'] '+eachZone.getName()+'\r\n')
            player.writeWithPrompt("")
        else:
            # TODO: Enable displaying of specific infoa bout a specified zone.
            # not sure what info yet...
            
            player.writeWithPrompt("Feature not yet implemented.")
        
            

