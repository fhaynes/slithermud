### 10-8-2007
### A "commands" Command
### By Adam "Vopisk" Dean

import MudCommand
import MudAction
import MudWorld

from exceptions import *

class cmdCommands(MudCommand.MudCommand):
    """
    This is the "commands" command.

    This should be fairly straightforward.  What we want to do is to display to users all
    the commands that they have available to them.

    Syntax is: commands
    """

    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "commands"
        self.info['helpText']   = '''This command shows the player a list of commands at their disposal.'''
        self.info['useExample'] = '''commands'''

    def process(self, player, args = ''):
        '''
        Changed this command so that everything that needs to happen, happens here, rather than
        in MudActionHandler.py.  This keeps the action handler from becoming ungainly with simple
        little functions like this.
        '''
        cmdList = player.getCommands()
        try:
            assert cmdList[0] != 0
        except:
            player.writeWithPrompt("And error has occurred in the Commands command, please notify an administrator.\r\n")
            print "No command list for" + player.getName()
        player.writeWithPrompt(', '.join(cmdList))
        