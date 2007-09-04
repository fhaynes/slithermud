import MudCommand
import MudAction
import MudActionHandler

import string

class cmdBuildWalk(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "buildwalk"
        self.helpText = '''This lets you create exits and rooms by walking.'''
        self.useExample = '''buildwalk'''
        
    def Process(self, player, args=''):
        if player.statistics.has_key('buildwalk'):
            if player.statistics['buildwalk'] == 0:
                player.writeWithPrompt("Buildwalk enabled!")
                player.statistics['buildwalk'] = 1
                return
            elif player.statistics['buildwalk'] == 1:
                player.writeWithPrompt("Buildwalk disabled!")
                player.statistics['buildwalk'] = 0
                return
            else:
                return
        else:
            player.statistics['buildwalk'] = 1
            player.writeWithPrompt("Buildwalk enabled!")
            return
        

        
        





      
buildwalk = cmdBuildWalk()