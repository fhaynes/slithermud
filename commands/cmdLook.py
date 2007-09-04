import MudCommand
import MudAction
import MudActionHandler
import MudDatabase

class cmdLook(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "look"
        self.helpText = '''This looks at your surroundings or at a specific thing.'''
        self.useExample = '''look (target)'''

    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'canlook'
        action.playerRef  = player
        action.string     = args
        MudActionHandler.actionHandler.doAction(action)
look = cmdLook()