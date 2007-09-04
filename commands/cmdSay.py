#!/usr/bin/python

### cmdSay.py
### (c)2004 Fletcher Haynes, All Rights Reserved
### 12-15-04

### This is the say command.

import MudCommand
import MudAction
import MudActionHandler

import string

class cmdSay(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "say"
        self.helpText   = '''Lets you say something to the room.'''
        self.useExample = '''say text'''
        
    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'cansay'
        action.playerRef  = player
        action.string     = args
        
        MudActionHandler.actionHandler.doAction(action)
      
say = cmdSay()