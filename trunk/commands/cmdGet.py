import MudCommand
import MudWorld
import MudAction
import MudActionHandler

import string

class cmdGet(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "get"
        self.helpText = '''This tries to get an item.'''
        self.useExample = '''get sword'''
        
    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'attemptgetitem'
        action.playerRef  = player
        if args == '':
            player.writeWithPrompt("Get what?")
            return
        args = args.split(" ")
        if len(args) == 1:
            action.data2 = 1
        if len(args) == 2:
            action.data2 = int(args[1])
        tmp = player.roomRef.findItem(args[0])
        if tmp == []:
            player.writeWithPrompt("Item not present.")
            return
        else:
            for eachItem in tmp:
                action.data1 = eachItem
                MudActionHandler.actionHandler.doAction(action)
                
        





      
get = cmdGet()