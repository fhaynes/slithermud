import MudCommand
import MudDatabase

import string

class cmdVari(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "vari"
        self.helpText   = '''Do not use this!!!'''
        self.useExample = '''vari'''
        
    def Process(self, player, args=''):
        z = MudDatabase.db.zones[1]
        for eachRoom in z.rooms.values():
            for eachPortal in eachRoom.portals.values():
                eachPortal.target_zone = 1
        player.writeWithPrompt("Done.")


vari = cmdVari()