#!/usr/bin/python

### cmdIcreate.py
### (c)2004 Fletcher Haynes, All Rights Reserved
### 12-15-04

import MudCommand
import MudAction
import MudActionHandler

class cmdMcreate(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "mcreate"
        self.helpText = '''This creates an character from a template.'''
        self.useExample = '''mcreate template_id'''

    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'spawncharacter'
        action.playerRef  = player
        action.data1      = int(args)
        MudActionHandler.actionHandler.doAction(action)
        
mcreate = cmdMcreate()