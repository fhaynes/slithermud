import MudCommand
import MudAction
import MudActionHandler
import MudDatabase

import string

class cmdTell(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "tell"
        self.helpText   = '''Sends a message to a specific player.'''
        self.useExample = '''tell Kuros You are wonderful!'''
        
    def Process(self, player, args=''):
        args = args.split(" ", 1)
        tmp = MudDatabase.db.findCharByName(args[0])
        if tmp == None:
            player.writeWithPrompt("Unable to find that character!")
            return
        
        player.writeWithPrompt('You tell '+tmp.name+', "'+args[1]+'"')
        tmp.writeWithPrompt(player.name+' tells you, "'+args[1]+'"')
        return
      
tell = cmdTell()