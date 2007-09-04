import MudDatabase
import MudCommand
import MudConst
class cmdSaveZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "savezone"
        self.helpText = '''This saves a zone.'''
        self.useExample = '''savezone zone ID'''


    def Process(self, player, args):
        try:
            # Make this more efficient
            zone = MudDatabase.db.zones[int(args)]
            tmp = open(MudConst.load_list, 'w')
            for eachZone in MudDatabase.db.zones.values():
                tmp.write(eachZone.name.replace(" ", "")+'\r\n')
            MudDatabase.db.saveZoneToDisk(zone)
        
            player.writeWithPrompt("Zone saved!")
            
        except:
            player.writeWithPrompt("That ID does not exist, or you did enter a zone ID! Do not use zone names!")
            return


        
        
                
        
 




savezone = cmdSaveZone()