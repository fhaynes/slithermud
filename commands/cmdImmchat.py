import MudCommand
import MudWorld

import string

class cmdImmChat(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "immchat"
        self.helpText   = '''Broadcasts a chat message to all connected staff.'''
        self.useExample = '''immchat message'''
        
    def Process(self, player, args=''):
        if args == '':
            player.writeWithPrompt("You must chat something!")
            return
        msg = '<bright><green>[IMM-CHAT] <r>'+player.name+' chats: '+args
        MudWorld.world.sendToImms(msg)
        
      
immchat = cmdImmChat()