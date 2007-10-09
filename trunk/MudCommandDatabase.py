import cmdLook
import cmdSay
import cmdGo
import cmdGet
import cmdDrop
import cmdVari
import cmdSearch
import cmdCommands
import cmdQuit

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
        self.commands['vari']        = cmdVari.cmdVari
        self.commands['search']      = cmdSearch.cmdSearch
        self.commands['commands']    = cmdCommands.cmdCommands
        self.commands['quit']        = cmdQuit.cmdQuit
        
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

    def getCommand(self, name):
        """Returns a new command instance."""
        return self.commands[name]()
    
    def loadAllCommand(self, player):
        """Gives all commands to the player. Takes a player reference."""
        for eachCmd in self.commands.keys():
            player.addCommand(eachCmd, self.commands[eachCmd]())