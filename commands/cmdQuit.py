import MudCommand
import MudWorld
import MudAction
import MudActionHandler
import MudDatabase

import string

class cmdQuit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "quit"
        self.helpText   = '''This causes you to exit the game.'''
        self.useExample = '''quit'''
        
    def Process(self, player, args=''):
        player.sockRef.loseConnection()


quit = cmdQuit()