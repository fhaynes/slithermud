import cmdLook
import cmdSay
import cmdGo

class CommandDatabase:
    def __init__(self):
        self.commands = {}
        self.commands['look'] = cmdLook.cmdLook
        self.commands['say'] = cmdSay.cmdSay
        self.commands['go'] = cmdGo.cmdGo
        
    def getCommand(self, name):
        """Returns a new command instance."""
        return self.commands[name]()
    
    def loadAllCommand(self, player):
        """Gives all commands to the player. Takes a player reference."""
        for eachCmd in self.commands.keys():
            player.addCommand(eachCmd, self.commands[eachCmd]())