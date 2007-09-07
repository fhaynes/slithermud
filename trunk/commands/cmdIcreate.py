import MudCommand
import MudAction
import MudActionHandler

class cmdIcreate(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "icreate"
        self.helpText   = '''This creates an item from a template.'''
        self.useExample = '''icreate templateid'''

    def Process(self, player, args=''):
        if not args.isdigit():
            player.writeWithPrompt("You must specify a template ID!")
            return
        action = MudAction.MudAction()
        action.actionType = 'spawnitem'
        action.playerRef  = player
        action.data1      = int(args[0])
        MudActionHandler.actionHandler.doAction(action)


icreate = cmdIcreate()