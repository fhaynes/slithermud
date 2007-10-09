import cmdLook
import cmdSay
import cmdGo
import cmdGet
import cmdDrop
import cmdVari
import cmdSearch
import cmdCommands

# OLC Related Imports
import cmdNewZone
import cmdDelZone
import cmdListZone
import cmdNewRoom
import cmdDelRoom

class CommandDatabase:
    def __init__(self):
        self.commands = {}
        self.commands['look']     = cmdLook.cmdLook
        self.commands['say']      = cmdSay.cmdSay
        self.commands['go']       = cmdGo.cmdGo
        self.commands['get']      = cmdGet.cmdGet
        self.commands['drop']     = cmdDrop.cmdDrop
        self.commands['vari']     = cmdVari.cmdVari
        self.commands['search']   = cmdSearch.cmdSearch
        self.commands['commands'] = cmdCommands.cmdCommands
        
        # ---------------------- #
        #  OLC Related Commands  #
        # ---------------------- #
        self.commands['newzone']  = cmdNewZone.cmdNewZone
        self.commands['delzone']  = cmdDelZone.cmdDelZone
        self.commands['listzone'] = cmdListZone.cmdListZone
        self.commands['newroom']  = cmdNewRoom.cmdNewRoom
        self.commands['delroom']  = cmdDelRoom.cmdDelRoom
        
    def getCommand(self, name):
        """Returns a new command instance."""
        return self.commands[name]()
    
    def loadAllCommand(self, player):
        """Gives all commands to the player. Takes a player reference."""
        for eachCmd in self.commands.keys():
            player.addCommand(eachCmd, self.commands[eachCmd]())