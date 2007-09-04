import MudCommand
import MudAction
import MudActionHandler
import MudDatabase

class cmdSearch(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "search"
        self.helpText = '''This lets you search for items and characters.'''
        self.useExample = '''search item/char/itemplate/ctemplate string'''

    def Process(self, player, args=''):
        args = args.split(" ", 1)
        if len(args) != 2:
            player.writeWithPrompt("Proper format is: search item/char/itemplate/ctemplate string!")
            return
        
        if args[0].lower() == 'item':
            res = MudDatabase.db.findItemsByName(args[1])
            if res == []:
                player.writeWithPrompt("No listing of that item found!")
                return
            else:
                x = 0
                for eachThing in res:
                    if x != 5:
                        player.writePlain('(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                        x = x + 1
                    else:
                        player.writePlain('\r\n(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                        x = 0
                player.writeWithPrompt("")
                return
        if args[0].lower() == 'char':
            res = MudDatabase.db.findCharsByName(args[1])
            if res == []:
                player.writeWithPrompt("No listing of that item found!")
                return
            else:
                x = 0
                for eachThing in res:
                    if x != 5:
                        player.writePlain('(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                        x = x + 1
                    else:
                        player.writePlain('\r\n(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                player.writeWithPrompt("")
                return
        if args[0].lower() == 'ctemplate':
            res = MudDatabase.db.findCharTemplateByName(args[1])
            if res == []:
                player.writeWithPrompt("No template listing of that template found!")
                return
            else:
                x = 0
                for eachThing in res:
                    if x != 5:
                        player.writePlain('(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                        x = x + 1
                    else:
                        player.writePlain('\r\n(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                player.writeWithPrompt("")
                return
        if args[0].lower() == 'itemplate':
            res = MudDatabase.db.findItemTemplateByName(args[1])
            if res == []:
                player.writeWithPrompt("No listing of that item template found!")
                return
            else:
                x = 0
                for eachThing in res:
                    if x != 5:
                        player.writePlain('(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                        x = x + 1
                    else:
                        player.writePlain('\r\n(['+str(eachThing.id_num)+'] ['+eachThing.name+'])   ')
                        x = 0
                player.writeWithPrompt("")
                return
        
        player.writeWithPrompt("You can search for: item char itemplate ctemplate!")
            



        
search = cmdSearch()