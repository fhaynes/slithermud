"""
cmdRevoke.py
Author: Fletcher Haynes
This command lets you revoke a command from a player.
"""

import MudCommand
import MudWorld
class cmdRevoke(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "revoke"
        self.info['helpText']   = '''Revokes a command from a player.'''
        self.info['useExample'] = '''revoke playername commandname'''
        
    def process(self, player, args=''):
        argList = args.split(" ")
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is revoke commandname.")
            return
        
        try:
            t = MudWorld.world.findPlayerByName(argList[0])
        except:
            player.writeWithPrompt("That player is not logged in.")
            return
        

        try:
            t.removeCommand(argList[1].lower())
            t.writeWithPrompt("Your: "+argList[1].lower()+" command was revoked!")
            player.writeWithPrompt("You revoked the "+argList[1]+" command from "+t.getName())
            return
        except:
            player.writeWithPrompt("The player does not have that command.")
            return
        