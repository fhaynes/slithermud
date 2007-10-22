import MudCommand
import MudWorld
class cmdGrant(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "grant"
        self.info['helpText']   = '''Grants a player a command or group of commands.'''
        self.info['useExample'] = '''grant playername all/olc/standard or grant playername commandname'''
        
    def process(self, player, args=''):
        argList = args.split(" ")
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is grant name group or commandname.")
            return
        
        try:
            t = MudWorld.world.findPlayerByName(argList[0])
        except:
            player.writeWithPrompt("That player is not logged in.")
            return
        
        if argList[1].lower() == 'all':
            MudWorld.world.cmdDb.loadAllCommand(t)
            player.writeWithPrompt("All commands granted to: "+t.getName())
            t.writeWithPrompt("You have been granted all commands by: "+player.getName())
            return
        elif argList[1].lower() == 'olc':
            MudWorld.world.cmdDb.loadOlcCommands(t)
            player.writeWithPrompt("OLC commands granted to: "+t.getName())
            t.writeWithPrompt("You have been granted OLC commands by: "+player.getName())
            return
        elif argList[1].lower() == 'standard':
            MudWorld.world.cmdDb.loadStdCommands(t)
            player.writeWithPrompt("Standard Admin commands granted to: "+t.getName())
            t.writeWithPrompt("You have been granted Standard Admin commands by: "+player.getName())
        else:
            if argList[1].lower() in MudWorld.world.cmdDb.getCommandList():
                t.addCommand(argList[1].lower(), MudWorld.world.cmdDb.getCommand(argList[1]))
                player.writeWithPrompt("Command: "+argList[1]+" granted to "+t.getName())
                t.writeWithPrompt("You were granted: "+argList[1]+" by "+player.getName())
            else:
                player.writeWithPrompt("That command was not found.")
                return