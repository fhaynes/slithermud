import MudCommand
import MudAction
import MudActionHandler
import MudProtocol
import autoreload
import sys
class cmdCopyover(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "copyover"
        self.helpText = '''This reloads all the code of the MUD'''
        self.useExample = 'copyover'

    def Process(self, player, args=''):
        autoreload.run()
        autoreload.stop()
        autoreload.superreload(MudProtocol)
        player.writeWithPrompt("Copyover complete!")

    




copyover = cmdCopyover()