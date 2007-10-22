import MudCommand
import MudAction
import MudWorld

import string

class cmdGo(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "go"
        self.helpText   = '''This tries to move you through a portal.'''
        self.useExample = '''go portalname'''
        
    def process(self, player, args=''):
        if args == '':
            player.writeWithPrompt("Go where?")
            return

        for eachPortal in player.getRoomRef().getPortals().values():
            if eachPortal.getName().lower() == args.lower():
                action = MudAction.MudAction('enterportal', player, eachPortal)
                MudWorld.world.actionHandler.doAction(action)
                return
        
        player.writeWithPrompt("Unable to find that portal.")
                    