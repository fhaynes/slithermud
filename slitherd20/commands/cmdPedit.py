"""
cmdPedit.py
Author: Fletcher Haynes
This command allows editing of portal attributes.
"""

import MudCommand
import MudWorld

import string
import os

class cmdPedit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "pedit"
        self.info['helpText']   = '''Lets you edit portal attributes'''
        self.info['useExample'] = '''pedit id (name, targetzone, targetroom)'''
        
    def process(self, player, args=''):
        
        argList = args.split(" ", 2)
        
        if len(argList) != 3:
            player.writeWithPrompt("Proper format is: pedit id field value.")
            return
        
        if not argList[0].isdigit():
            player.writeWithPrompt("Proper format is: pedit id field value.")
            
        # Let's get the portal and room reference
        r = player.getRoomRef()
        try:
            p = r.getPortal(int(argList[0]))
        except KeyError:
            player.writeWithPrompt("No portal with that ID exists in this room.")
            return
            
        if argList[1].lower() == 'name':
            p.setName(argList[1])
            player.writeWithPrompt("Portal name changed.")
            return
        
        elif argList[1].lower() == 'targetroom':
            if not argList[2].isdigit():
                player.writeWithPrompt("Target Room IDs must be numbers.")
                return
            p.setTargetRoom(int(argList[2]))
            return
        
        elif argList[1].lower() == 'targetzone':
            if not argList[2].isdigit():
                player.writeWithPrompt('Target Zone IDs must be numbers.')
                return
            p.setTargetZone(int(argList[2]))
            return
        elif argList[1].lower() == 'addlogic':
            try:
                name, logic = MudWorld.world.logicDb.getLogic(argList[2])
                p.addLogic(name, logic)
                player.writeWithPrompt("Logic module added to portal.")
                return
            except:
                player.writeWithPrompt("Could not find that logic module.")
                return
        elif argList[1].lower() == 'dellogic':
            try:
                p.removeLogic(argList[2])
            except KeyError:
                player.writeWithPrompt("That logic module is not attached to this portal.")
                return
        else:
            player.writeWithPrompt("That is not a valid field to edit.")
            return
            

