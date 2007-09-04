import MudDatabase
import MudZone
import MudRoom
import MudCommand
import MudConst

class cmdDelZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "delzone"
        self.helpText = '''This removes a zone from disk.'''
        self.useExample = '''delzone New Zone Name'''


    def Process(self, player, args):
        try:
            MudDatabase.db.deleteZoneFromDisk(args)
            player.writeWithPrompt("Zone has been deleted!")
            tmp = open(MudConst.load_list, 'w')
            for eachZone in MudDatabase.db.zones.values():
                tmp.write(eachZone.name.replace(" ", "")+'\r\n')
            return
        except OSError: 
            player.writeWithPrompt("Invalid zone name!")
            return
        
 




delzone = cmdDelZone()