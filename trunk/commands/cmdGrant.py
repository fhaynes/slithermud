import MudCommand
import MudWorld
import MudAction
import MudActionHandler
import MudDatabase

import sys
import string

class cmdGrant(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "grant"
        self.helpText   = '''This grants a command to a user.'''
        self.useExample = '''grant Kuros info'''
        
    def Process(self, player, args=''):
        args = args.split(" ")
        if len(args) != 2:
            player.writeWithPrompt("Proper format is grant player command!")
            return
        tmp = MudDatabase.db.findCharByName(args[0])
        if tmp == None:
            player.writeWithPrompt("Could not find that player!")
            return
        if tmp.commands.has_key(args[1].lower()):
            tmp.removeCommand(args[1].lower())
            player.writeWithPrompt("Command has been removed from player!")
            return
        if MudDatabase.db.commands.has_key(args[1].lower()):
            tmp.addCommand(args[1].lower(), MudCommandDatabase.CommandDB.commands[args[1].lower()])
            player.writeWithPrompt("Command has been granted!")


grant = cmdGrant()