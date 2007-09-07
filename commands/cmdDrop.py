import MudCommand
import MudWorld
import MudAction
import MudActionHandler

import string

class cmdDrop(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "drop"
        self.helpText   = '''This tries to drop an item.'''
        self.useExample = '''drop sword'''
        
    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'attemptdropitem'
        action.playerRef  = player
        if args == '':
            player.writeWithPrompt("Drop what?")
            return
        args = args.split(" ")
        if len(args) == 1:
            action.data2 = 1
        if len(args) == 2:
            action.data2 = int(args[1])
        x = 0
        for eachItem in player.items.values():
            if args[0].lower() in eachItem.name.lower():
                action.data1 = eachItem
                x = 1
                MudActionHandler.actionHandler.doAction(action)
        if x == 0:
            player.writeWithPrompt("You do not have that item!")

  
drop = cmdDrop()