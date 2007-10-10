"""
cmdSpawn.py
Author: Fletcher Haynes
Lets you spawn an instance of a character or item template.
"""

import MudCommand
import MudWorld
import MudAction

import string
import os

class cmdSpawn(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "spawn"
        self.info['helpText']   = "Spawn allows you to create an instance from a character or item template. \
        The instance is created in the room you are in."
        self.info['useExample'] = "spawn character/item 5"
        
    def process(self, player, args=''):
        argList = args.split(" ")
        print argList
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is spawn character/item TemplateID.")
            return

        if not argList[1].isdigit():
            player.writeWithPrompt("ID Numbers must be numerical.")
            return
        
        if argList[0].lower() == 'character':
            try:
                action = MudAction.MudAction('spawncharacter', player, \
                int(argList[1]), player.getZoneRef().getId(), \
                player.getRoomRef().getId())
                MudWorld.world.actionHandler.doAction(action)
                player.writeWithPrompt("You spawned a character from ID: "+str(argList[1]))
                return
            except KeyError:
                player.writeWithPrompt("That character template ID does not exist.")
                return
        elif argList[0].lower() == 'item':
            try:
                action = MudAction.MudAction('spawnitem', player, \
                int(argList[1]), player.getZoneRef().getId(), \
                player.getRoomRef().getId())
                MudWorld.world.actionHandler.doAction(action)
                player.writeWithPrompt("You spawned an item from ID: "+str(argList[1]))
                return
            except KeyError:
                player.writeWithPrompt("That item template ID does not exist.")
                return
        else:
            player.writeWithPrompt("You can only spawn items or characters.")
            return
        
        
        

        

