# A change to test copyover functionality! - Vopisk
# Again!

import cmdLook
import cmdSay
import cmdGo
import cmdGet
import cmdDrop
import cmdCommands
import cmdQuit
import cmdColor
import cmdCredits

# OLC Related Imports
import cmdNewZone
import cmdDelZone
import cmdListZone
import cmdNewRoom
import cmdDelRoom
import cmdRedit
import cmdNewPortal
import cmdDelPortal
import cmdZedit
import cmdPedit
import cmdNewTemplate

# Admin Related Imports
import cmdWarp
import cmdEdit
import cmdSpawn
import cmdAddStat
import cmdDelStat
import cmdVari
import cmdSearch
import cmdGrant
import cmdRevoke
import cmdInfo
import cmdCopyover
import cmdSaveZone
import cmdObliterate

class CommandDatabase:
    def __init__(self):
        
        # ---------------------------- #
        # General Commands for Players #
        # ---------------------------- #
        self.commands = {}
        self.commands['look']        = cmdLook.cmdLook
        self.commands['say']         = cmdSay.cmdSay
        self.commands['go']          = cmdGo.cmdGo
        self.commands['get']         = cmdGet.cmdGet
        self.commands['drop']        = cmdDrop.cmdDrop
        self.commands['commands']    = cmdCommands.cmdCommands
        self.commands['quit']        = cmdQuit.cmdQuit
        self.commands['color']       = cmdColor.cmdColor
        self.commands['credits']     = cmdCredits.cmdCredits
        
        # ---------------------- #
        #  OLC Related Commands  #
        # ---------------------- #
        self.commands['newzone']     = cmdNewZone.cmdNewZone
        self.commands['delzone']     = cmdDelZone.cmdDelZone
        self.commands['listzone']    = cmdListZone.cmdListZone
        self.commands['newroom']     = cmdNewRoom.cmdNewRoom
        self.commands['redit']       = cmdRedit.cmdRedit
        self.commands['delroom']     = cmdDelRoom.cmdDelRoom
        self.commands['newportal']   = cmdNewPortal.cmdNewPortal
        self.commands['delportal']   = cmdDelPortal.cmdDelPortal
        self.commands['zedit']       = cmdZedit.cmdZedit
        self.commands['pedit']       = cmdPedit.cmdPedit
        self.commands['newtemplate'] = cmdNewTemplate.cmdNewTemplate
        
        # ---------------------- #
        # Admin Related Commands #
        # ---------------------- #
        self.commands['warp']        = cmdWarp.cmdWarp
        self.commands['edit']        = cmdEdit.cmdEdit
        self.commands['spawn']       = cmdSpawn.cmdSpawn
        self.commands['vari']        = cmdVari.cmdVari
        self.commands['search']      = cmdSearch.cmdSearch
        self.commands['addstat']     = cmdAddStat.cmdAddStat
        self.commands['delstat']     = cmdDelStat.cmdDelStat
        self.commands['grant']       = cmdGrant.cmdGrant
        self.commands['revoke']      = cmdRevoke.cmdRevoke
        self.commands['info']        = cmdInfo.cmdInfo
        self.commands['copyover']    = cmdCopyover.cmdCopyover
        self.commands['savezone']    = cmdSaveZone.cmdSaveZone
        self.commands['obliterate']  = cmdObliterate.cmdObliterate

    def getCommand(self, name):
        """Returns a new command instance."""
        return self.commands[name]()
    
    def getCommandList(self):
        """Returns all the keys in the command dictionary."""
        return self.commands.keys()
    
    def loadAllCommand(self, player):
        """Gives all commands to the player. Takes a player reference."""
        for eachCmd in self.commands.keys():
            player.addCommand(eachCmd, self.commands[eachCmd]())
            
    def loadOlcCommands(self, player):
        """Gives all OLC commands to the player. Takes a player reference."""
        player.addCommand('newzone', self.commands['newzone']())
        player.addCommand('delzone', self.commands['delzone']())
        player.addCommand('listzone', self.commands['listzone']())
        player.addCommand('newroom', self.commands['newroom']())
        player.addCommand('redit', self.commands['redit']())
        player.addCommand('delroom', self.commands['delroom']())
        player.addCommand('newportal', self.commands['newportal']())
        player.addCommand('delportal', self.commands['delportal']())
        player.addCommand('zedit', self.commands['zedit']())
        player.addCommand('pedit', self.commands['pedit']())
        player.addCommand('newtemplate', self.commands['newtemplate']())
    
    def loadStdCommands(self, player):
        """Loads standard admin commands."""
        player.addCommand('spawn', self.commands['spawn']())
        player.addCommand('edit', self.commands['edit']())
        player.addCommand('search', self.commands['search']())
        player.addCommand('warp', self.commands['warp']())
        player.addCommand('addstat', self.commands['addstat']())
        player.addCommand('delstat', self.commands['delstat']())
        player.addCommand('savezone', self.commands['savezone']())
        player.addCommand('obliterate', self.commands['obliterate']())
        
    def loadPlayerCommands(self, player):
        """Loads player specific commands."""
        player.addCommand('get', self.commands['get']())
        player.addCommand('drop', self.commands['drop']())
        player.addCommand('go', self.commands['go']())
        player.addCommand('say', self.commands['say']())
        player.addCommand('look', self.commands['look']())
        player.addCommand('quit', self.commands['quit']())
        player.addCommand('commands', self.commands['commands']())
        player.addCommand('color', self.commands['color']())