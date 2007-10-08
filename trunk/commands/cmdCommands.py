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
        Shouldn't be much processing here, just need to query the player for their list of commands,
        then retun that list in a nicely formatted fashion.
        '''
        cmdList = player.getCommands()
        action = MudAction.MudAction('commands', player, cmdList, '', '', args)
        MudWorld.world.processAction(action)
        