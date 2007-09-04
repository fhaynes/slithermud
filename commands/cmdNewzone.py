import MudDatabase
import MudZone
import MudRoom
import MudCommand

class cmdNewZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "newzone"
        self.helpText = '''This lets you create a new zone in the game.'''
        self.useExample = '''newzone New Zone Name'''


    def Process(self, player, args):
        if args == '':
            player.writeWithPrompt("Please specify a zone name!")
            return
        if not args[1].isalpha():
            player.writeWithPrompt("Zone names can only contain letters and spaces!")
            return
        
        if MudDatabase.db.checkZoneNameExists(args[1]):
            player.writeWithPrompt("That zone name is already in use!")
            return
        
        newZone = MudZone.MudZone()
        newZone.allowed.append(player.name)
        newZone.id_num = MudDatabase.db.generateNextId('zone')
        newZone.name   = args
        MudDatabase.db.addZone(newZone)
        
        newRoom = MudRoom.MudRoom()
        newRoom.id_num = 1
        newRoom.addLogic('basicRoomLogic')
        newZone.addRoom(newRoom)
        
        player.writeWithPrompt("Zone added!")
        
                
        
 




newzone = cmdNewZone()