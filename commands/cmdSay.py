#!/usr/bin/python

### cmdSay.py
### (c)2004 Fletcher Haynes, All Rights Reserved
### 12-15-04

### This is the say command.

import MudCommand
import MudAction
import MudWorld

import string

class cmdSay(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "say"
        self.info['helpText']   = '''Lets you say something to the room.'''
        self.info['useExample'] = '''say text'''
        
    def process(self, player, args=''):
        action = MudAction.MudAction('say', player, '', '', '', args)
        MudWorld.world.processAction(action)
