#!/usr/bin/python

### cmdOlc.py
### (c)2004 Fletcher Haynes, All Rights Reserved
### 12-15-04

### This is the say command.

import MudCommand
import MudAction
import MudActionHandler
import MudConst
import MudWorld

import string

class cmdOlc(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "olc"
        self.helpText   = '''This allows you to enter the OLC system.'''
        self.useExample = '''olc'''


    def Process(self, player, args=''):

        player.writePlain("Entering the OLC system!\r\n")
        player.login_state = MudConst.inOlc
        MudWorld.world.olcHandler.addUser(player)
        
        
        
      
olc = cmdOlc()