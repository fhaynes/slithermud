import MudCommand
import MudWorld
import MudAction
import MudActionHandler
import MudDatabase

import string

class cmdAssign(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "assign"
        self.helpText   = '''This assigns vnums to a character.'''
        self.useExample = '''assign Kuros item/mob 100 150'''
        
    def Process(self, player, args=''):
        args = args.split(" ")
        if len(args) != 4:
            player.writeWithPrompt("Proper format is: assign name item/mob lowvnum highvnum!")
            return
        if not args[2].isdigit():
            player.writeWithPrompt("Only numbers are allowed for vnums!")
            return
        if not args[3].isdigit():
            player.writeWithPrompt("Only numbers are allowed for vnums!")
            return
        t = MudDatabase.db.findCharByName(args[0])
        if t == None:
            player.writeWithPrompt("Could not find that player!")
            return
        if t.sockRef == '':
            player.writeWithPrompt("Can only assign vnums to players!")
            return
        
        if args[1].lower() == 'item':
            t.statistics['i_lvnum'] = int(args[2])
            t.statistics['i_hvnum'] = int(args[3])
        elif args[1].lower() == 'mob':
            t.statistics['m_lvnum'] = int(args[2])
            t.statistics['m_hvnum'] = int(args[3])
            
        else:
            player.writeWithPrompt("You must choose to assign item or mob vnums!")
            return
        
        player.writeWithPrompt("Vnums have been assigned!")
        
   
assign = cmdAssign()