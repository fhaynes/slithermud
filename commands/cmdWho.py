import MudCommand
import MudAction
import MudActionHandler
import MudConst
import MudWorld

import string

class cmdWho(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "who"
        self.helpText   = '''This lets you see who is online.'''
        self.useExample = '''who'''


    def Process(self, player, args=''):
        player.writePlain('\r\n<red>[===============PLAYERS ONLINE===============]<r>')
        for eachPlayer in MudWorld.world.databaseHandler.characters.values():
            if eachPlayer.sockRef != '':
                if eachPlayer.admin_level == MudConst.player:
                    player.writePlain('\r\n'+eachPlayer.name)
                if eachPlayer.admin_level == MudConst.builder:
                    player.writePlain('\r\n'+eachPlayer.name+'<green>          [BUILDER]<r>')
                if eachPlayer.admin_level == MudConst.implementor:
                    player.writePlain('\r\n'+eachPlayer.name+'<cyan>           [IMPLEMENTOR]<r>')

        player.writePlain('\r\n\r\n<red>[============================================]<r>\r\n')
        player.writeWithPrompt("")
        
        
        
      
who = cmdWho()