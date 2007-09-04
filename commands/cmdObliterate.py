import MudCommand
import MudAction
import MudActionHandler
import MudDatabase

class cmdObliterate(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "obliterate"
        self.helpText = '''This removes an item or mob from the game, and from disk.'''
        self.useExample = '''obliterate item/mob id'''

    def Process(self, player, args=''):
        args = args.split(" ")
        if len(args) != 2:
            player.writeWithPrompt("Proper format is: obliterate item/mob id!")
            return
        if not args[1].isdigit():
            player.writeWithPrompt("IDs must be numbers only!")
            return
        
        if args[0].lower() == 'item':
            tmp = MudDatabase.db.findItem(args[1])
            if tmp == None:
                player.writeWithPrompt("Could not find that item!")
            else:
                action = MudAction.MudAction()
                action.actionType = 'destroyitem'
                action.playerRef  = player
                action.data1      = tmp
                MudActionHandler.actionHandler.doAction(action)
                
        elif args[0].lower() == 'mob':
            tmp = MudDatabase.db.findChar(args[1])
            if tmp == None:
                player.writeWithPrompt("Could not find that mob!")
            else:
                action = MudAction.MudAction()
                action.actionType = 'destroychar'
                action.playerRef  = player
                action.data1      = tmp
                MudActionHandler.actionHandler.doAction(action)
                
        else:
            player.writeWithPrompt("You can only obliterate items or mobs!")
            
obliterate = cmdObliterate()