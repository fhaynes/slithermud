import MudCommand
import MudWorld
import MudAction
import MudActionHandler
import MudDatabase

import string

class cmdInfo(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "info"
        self.helpText   = '''This displays info about an item, character, room or zone. Use search to get ids.'''
        self.useExample = '''info item/char/zone/room/portal id'''
        
    def Process(self, player, args=''):
        args = args.split(" ", 2)
        if len(args) < 2:
            player.writeWithPrompt("Proper format is: info item/char/zone/room/portal id!")
            return
        if not args[1].isdigit():
            player.writeWithPrompt("IDs must be numbers!")
            return
        if args[0].lower() == 'item':
            tmp = MudDatabase.db.findItem(args[1])
            if tmp == None:
                player.writeWithPrompt("Could not find that item!")
                return
            else:
                player.writePlain("<bright><green>INFO FOR: "+tmp.name+'<r>\r\n')
                player.writePlain("<cyan>[ID   ]  <green>"+str(tmp.id_num)+'\r\n<r>')
                player.writePlain("<cyan>[Name ]  <green>"+tmp.name+'\r\n<r>')
                player.writePlain("<cyan>[Desc ]  <green>"+tmp.desc+'\r\n<r>')
                player.writePlain("<cyan>[Stats]\r\n<r>")
                for eachStat in tmp.statistics.keys():
                    player.writePlain('<green>'+eachStat+' : '+str(tmp.statistics[eachStat])+'\r\n')
                player.writeWithPrompt("")
                return
        elif args[0].lower() == 'char':
            tmp = MudDatabase.db.findChar(args[1])
            if tmp == None:
                player.writeWithPrompt("Could not find that character!")
                return
            else:
                player.writePlain("<bright><green>INFO FOR: "+tmp.name+'<r>\r\n')
                player.writePlain("<cyan>[ID   ]  <green>"+str(tmp.id_num)+'\r\n<r>')
                player.writePlain("<cyan>[Name ]  <green>"+tmp.name+'\r\n<r>')
                player.writePlain("<cyan>[Desc ]  <green>"+tmp.desc+'\r\n<r>')
                player.writePlain("<cyan>[TID  ]  <green>"+str(tmp.template_id)+'\r\n<r>')
                player.writePlain("<cyan>[Stats]\r\n<r>")
                x = 0
                for eachStat in tmp.statistics.keys():
                    if x == 4:
                        player.writePlain('<green>'+eachStat+' : '+str(tmp.statistics[eachStat])+'\r\n')
                        x =0
                    else:
                        player.writePlain('<green>'+eachStat+' : '+str(tmp.statistics[eachStat])+'    ')
                        x = x + 1
                player.writePlain("<cyan>[Commands]<r>\r\n")
                x = 0
                for eachCommand in tmp.commands.values():
                    if x == 5:
                        player.writePlain(eachCommand.cmdName+'\r\n')
                        x = 0
                    else:
                        player.writePlain(eachCommand.cmdName+' ')
                        x = x + 1
                player.writeWithPrompt("")
                return
        elif args[0].lower() == 'zone':
            player.writeWithPrompt("Feature not yet implemented.")
            return
        elif args[0].lower() == 'room':
            player.writeWithPrompt("Feature not yet implemented.")
            return
        elif args[0].lower() == 'portal':
            player.writeWithPrompt("Feature not yet implemented.")
            return
        else:
            player.writeWithPrompt("You can only info items, chars, zones, rooms, or portals!")
            return


info = cmdInfo()