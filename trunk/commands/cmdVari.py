import MudCommand
import MudAction
import MudActionHandler
import MudDatabase
import MudWorld

import MudCharacter
class cmdVari(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "vari"
        self.info['helpText']   = '''DO NOT USE!'''
        self.info['useExample'] = '''DO NOT USE!'''
        
    def process(self, player, args=''):
        action = MudAction.TimedAction('look', player, '', '', '', args)
        MudWorld.world.actionHandler.addActionRelative(action, 10)
        
        