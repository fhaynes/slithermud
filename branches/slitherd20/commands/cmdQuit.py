"""
cmdQuit.py
Author: Fletcher Haynes
This command allows the player to quit.
"""

import MudCommand
import MudWorld
import MudAction

import string
import os

class cmdQuit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "quit"
        self.info['helpText']   = '''Lets you quit the game.'''
        self.info['useExample'] = '''quit'''
        
    def process(self, player, args=''):
        newAction = MudAction.MudAction('leaveworld', player)
        MudWorld.world.actionHandler.doAction(newAction)

