import MudCommand
import MudAction
import MudActionHandler
import MudDatabase
import MudWorld

class cmdLook(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "look"
        self.info['helpText']   = '''Look at your surroundings, or something specific.'''
        self.info['useExample'] = '''look (target)'''
        
    def process(self, player, args=''):
        action = MudAction.MudAction('look', player, '', '', '', args)
        MudWorld.world.processAction(action)