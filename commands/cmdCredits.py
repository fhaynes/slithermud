import MudCommand
import MudConst

class cmdCredits(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "credits"
        self.info['helpText']   = '''Displays the MUD credits'''
        self.info['useExample'] = '''credits'''
        
    def process(self, player, args=''):
        file = open(MudConst.creditFile, 'r')
        for eachLine in file.readlines():
            player.writePlain(eachLine)
        player.writeWithPrompt("")
