#!/usr/bin/python

### cmdSet.py
### (c)2004 Fletcher Haynes, All Rights Reserved
### 12-15-04

### This is the look command. It returns the room name, desc, and all visible stuff in it.

import MudCommand
import MudAction
import MudActionHandler

class cmdSet(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName     = "set"
        self.helpText    = '''This lets you set, add, or remove the attributes of things.'''
        self.useExample  = '''set char 10 strength 100'''
        self.useExample += '''\r\n set new char 10 strength 100'''
        self.useExample += '''\r\n set del char 10 strength'''
        self.useExample += '''\r\n set char 10 strength 100'''
        self.useExample += '''\r\n set item 10 name sword'''

    def Process(self, player, args=''):
        args = args.split(" ")
        if len(args) == 4:
            if args[0].lower() == 'del':
                if args[2].isdigit():
                    args[2] = int(args[2])
                action = MudAction.MudAction()
                action.actionType = 'delstat'
                action.playerRef  = player
                action.data1      = args[1]
                action.data2      = args[2]
                action.data3      = args[3]
                MudActionHandler.actionHandler.doAction(action)
                return
            if args[3].isdigit():
                args[3] = int(args[3])
            action = MudAction.MudAction()
            action.actionType = 'modifystat'
            action.playerRef  = player
            action.data1      = args[0] # Type of entity to modify (item, char, etc)
            action.data2      = args[1] # ID of entity to modify
            action.data3      = args[2] # Name of stat to set
            action.string     = args[3] # Value to set stat at
            MudActionHandler.actionHandler.doAction(action)
            
            
        elif len(args) == 5:
            if args[0].lower() == 'new':
                if args[4].isdigit():
                    args[4] = int(args[4])
                action = MudAction.MudAction()
                action.actionType = 'addstat'
                action.playerRef  = player
                action.data1      = args[1]
                action.data2      = args[2]
                action.data3      = args[3]
                action.string     = args[4]
                MudActionHandler.actionHandler.doAction(action)
            else:
                player.writeWithPrompt("Proper usage is set (new or del) type id stat (value)!")
                
        else:
            player.writeWithPrompt("Proper usage is: set (new/del) type id stat value!")


set = cmdSet()