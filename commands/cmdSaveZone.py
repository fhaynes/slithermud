"""
cmdSaveZone.py
Author: Fletcher Haynes
This file handles manually saving a zone.
"""

import MudCommand
import MudWorld

import string
import os

class cmdSaveZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "savezone"
        self.info['helpText']   = '''Saves the zone with the supplied ID number.'''
        self.info['useExample'] = '''savezone 3'''
        
    def process(self, player, args=''):
        if args == '':
            player.writeToSelf("Please specify a zone ID.")
            return
        try:
            name = MudWorld.world.getZone(int(args)).getName()
            MudWorld.world.removeZone(int(args))
        except KeyError:
            player.writeWithPrompt("A zone with that ID does not exist.")
            
        MudWorld.world.db.saveZone(MudWorld.world.getZone(int(args)))
        
        player.writeWithPrompt("Zone: "+name+" has been saved!")
        
            

