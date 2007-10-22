"""
cmdZedit.py
Author: Fletcher Haynes
This command allows editing of room attributes.
"""

import MudCommand
import MudWorld

import string
import os

class cmdZedit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "zedit"
        self.info['helpText']   = '''Lets you edit the zone attributes.'''
        self.info['useExample'] = '''zedit (addlogic, dellogic)'''
        
    def process(self, player, args=''):
        # Let's split the args up. We only want to split it once, as the
        # parameter will always be one word, whereas the value might be
        # more than one. Such as: Zedit name Room of Superdeath.
        
        argList = args.split(" ", 1)
        
        # We always want 2 pieces of text. If there is only one, then
        # they didn't include a value.
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is: zedit field value.")
            return
        
        # Let's get the zone reference...
        
        # TODO: Do we want to allow them to edit zone names? That will require
        # deleting the old file, and rewriting the zone index. Not too hard,
        # but I am not sure I want to allow that. It might be safer to force
        # them to use delzone?
        z = player.getZoneRef()
        if argList[0].lower() == 'addlogic':
            try:
                name, logic = MudWorld.world.logicDb.getLogic(argList[1])
                r.addLogic(name, logic)
                player.writeWithPrompt("Logic module added to zone.")
                return
            except:
                player.writeWithPrompt("That logic module is not attached to this zone.")
                return
        elif argList[0].lower() == 'dellogic':
            try:
                r.removeLogic(argList[1])
            except KeyError:
                player.writeWithPrompt("That logic module is not attached to this zone.")
                return
        else:
            player.writeWithPrompt("That is not a valid field to edit.")
            return
            

