import MudPortal
import MudCommand

class cmdNewPortal(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "newportal"
        self.helpText = '''This lets you create a new exit from the room you are in.'''
        self.helpText += '''\r\nUse edit portal to edit target room/zone.'''
        self.useExample = '''newportal Portal Name'''


    def Process(self, player, args=''):
        if args == '':
            player.writeWithPrompt("You must give a name for the portal!")
            return
        
        newPortal = MudPortal.MudPortal()
        newPortal.name = args
        newPortal.target_zone = player.zone
        newPortal.id_num = player.zoneRef.generateNextPortalId()
        player.roomRef.addPortal(newPortal)
        player.writeWithPrompt("Portal added!")
        return
        
                
        
 




newportal = cmdNewPortal()