import MudCommand
import MudDatabase

import string

class cmdZoneList(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "zonelist"
        self.helpText = '''This lists all the zones in the game.'''
        self.useExample = '''zonelist'''
        
    def Process(self, player, args=''):
        x = 0
        for eachZone in MudDatabase.db.zones.values():
            player.writePlain('['+str(eachZone.id_num)+'] ['+eachZone.name+']\r\n')
            
        player.writeWithPrompt("")





      
zonelist = cmdZoneList()