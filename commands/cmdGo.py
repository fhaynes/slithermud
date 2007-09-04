import MudCommand
import MudAction
import MudActionHandler

import string

class cmdGo(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "go"
        self.helpText = '''This tries to move you through a portal.'''
        self.useExample = '''go portalname'''
        
    def Process(self, player, args=''):
        action = MudAction.MudAction()
        action.actionType = 'attemptenterportal'
        action.playerRef  = player
        action.data1      = args
        if action.data1 == '':
            action.playerRef.writeWithPrompt('Go where?')
            return
        MudActionHandler.actionHandler.doAction(action)
        
        





      
go = cmdGo()