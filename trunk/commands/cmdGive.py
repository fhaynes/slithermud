import MudCommand
import MudWorld
import MudAction
import MudActionHandler
import MudDatabase

import string

class cmdGive(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "give"
        self.helpText = '''This attempts to give a character an item.'''
        self.useExample = '''Give Kuros Sword (quantity)'''
        
    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'attemptgiveitem'
        action.playerRef  = player
        if args == '':
            player.writeWithPrompt("Give what!?")
            return
        args = args.split(" ")
        if len(args) == 2:
            action.data3 = 1
        elif len(args) == 3:
            action.data3 = int(args[2])
        else:
            player.writeWithPrompt("Proper format is: give player item (quantity)!")
            return
        
        x = 0
        
        if MudDatabase.db.findCharByName(args[0]):
            action.data1 = MudDatabase.db.findCharByName(args[0])
        else:
            player.writeWithPrompt("Give to whom?")
            return
        for eachItem in player.items.values():
            if args[1].lower() in eachItem.name.lower():
                action.data2 = eachItem
                x = 1
                MudActionHandler.actionHandler.doAction(action)
        if x == 0:
            player.writeWithPrompt("You do not have that item!")
                
        





      
give = cmdGive()