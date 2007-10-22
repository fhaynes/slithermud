"""
cmdRedit.py
Author: Fletcher Haynes
This command allows editing of room attributes.
"""

import MudCommand
import MudWorld

import string
import os

class cmdRedit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "redit"
        self.info['helpText']   = '''Lets you edit the room attributes.'''
        self.info['useExample'] = '''redit (name, desc, addlogic, dellogic)'''
        
    def process(self, player, args=''):
        # Let's split the args up. We only want to split it once, as the
        # parameter will always be one word, whereas the value might be
        # more than one. Such as: redit name Room of Superdeath.
        
        argList = args.split(" ", 1)
        
        # We always want 2 pieces of text. If there is only one, then
        # they didn't include a value.
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is: redit field value.")
            return
        
        # Let's get the room reference...
        r = player.getRoomRef()
        # Four things can be editedin the room. Let's handle each of them.
        if argList[0].lower() == 'name':
            r.setName(argList[1])
            player.writeWithPrompt("Room name changed.")
            return
        elif argList[0].lower() == 'desc':
            # TODO: Possibly allow for adding lines individually?
            r.setDesc(argList[1])
            player.writeWithPrompt("Room desc changed.")
            return
        elif argList[0].lower() == 'addlogic':
            try:
                name, logic = MudWorld.world.logicDb.getLogic(argList[1])
                r.addLogic(name, logic)
                player.writeWithPrompt("Logic module added to room.")
                return
            except:
                player.writeWithPrompt("Could not find that logic module.")
                return
        elif argList[0].lower() == 'dellogic':
            try:
                r.removeLogic(argList[1])
            except KeyError:
                player.writeWithPrompt("That logic module is not attached to this room.")
                return
        else:
            player.writeWithPrompt("That is not a valid field to edit.")
            return
            

