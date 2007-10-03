import MudCommand
import MudWorld
import MudAction

import string

class cmdGet(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "get"
        self.helpText   = '''This tries to get an item.'''
        self.useExample = '''get sword'''
        
    def process(self, player, args=''):
        if args == '':
            player.writeWithPrompt("Get what?")
            return
        action = MudAction.MudAction('getitem', player)
        args = args.split(" ")
        if args[0].isdigit():
            action.setData2(int(args[0]))
            name = str(args[1:])
        else:
            action.setData2(1)
            name = " ".join(str(x) for x in args)

        tmp = player.getRoomRef().findItemByName(name)
    
        if tmp == None:
            player.writeWithPrompt("Item not present.")
            return
        else:
            action.setData1(tmp)
            MudWorld.world.actionHandler.doAction(action)