import MudDatabase
import MudCommand

class cmdRemoveZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "removezone"
        self.helpText   = '''This removes a zone from the game. It does not delete it or keep it from loading on the next startup.'''
        self.useExample = '''removezone zone ID'''


    def Process(self, player, args):
        try:
            zone = MudDatabase.db.zones[int(args)]
        except:
            player.writeWithPrompt("That ID does not exist!")
            return

        MudDatabase.db.removeZone(zone)
        
        player.writeWithPrompt("Zone removed!")


removezone = cmdRemoveZone()