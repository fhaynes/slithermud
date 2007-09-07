import MudCommand
import MudAction
import MudActionHandler
import MudConst
import MudWorld

import string

class cmdHelp(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "help"
        self.helpText   = '''This gives you information on commands and other topics.'''
        self.useExample = '''help (command name/topic)'''
        


    def Process(self, player, args=''):
        
        if args == '':
            tmp = []
            for x in player.commands.values():
                tmp.append(x.cmdName)
            tmp.sort()
            y = 0
            l = 0
            for x in tmp:
                if len(x) > l:
                    l = len(x)
            for x in tmp:
                if y == 4:
                    player.writePlain(x+'\r\n')
                    y = 0
                else:
                    z = l - len(x)
                    player.writePlain(x)
                    for a in range(z):
                        player.writePlain(" ")
                    player.writePlain("   ")
                    y = y + 1   
        else:
            for eachCommand in player.commands.values():
                if eachCommand.cmdName.strip() == args.lower():
                    player.writePlain('\r\n<green>HELP FOR: '+eachCommand.cmdName+'<r>\r\n\r\n')
                    player.writePlain('Optional arguments are enclosed in ()<r>\r\n\r\n')
                    player.writePlain('<cyan>'+eachCommand.helpText+'<r>\r\n')
                    player.writePlain('<green>Usage: '+eachCommand.useExample+'<r>')
                    player.writeWithPrompt("")
                    
                    return
            player.writeWithPrompt("Invalid choice for help!")
        player.writeWithPrompt("")


help = cmdHelp()