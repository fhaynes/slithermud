import MudCommand
import MudAction
import MudActionHandler
import MudDatabase
import string

class cmdWarp(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "warp"
        self.helpText   = '''This teleports you directly to a zone and room.'''
        self.useExample = '''warp zoneid roomid or warp roomid or warp charname'''
        
    def Process(self, player, args=''):
        if args.isalpha():
            tmp = MudDatabase.db.findCharByName(args)
            if tmp == None:
                player.writeWithPrompt("Could not find that character!")
                return
            else:
                t_z = tmp.zone
                t_r = tmp.room
                newAction = MudAction.MudAction()
                newAction.actionType = 'forcetransport'
                newAction.playerRef  = player
                newAction.data1      = t_z
                newAction.data2      = t_r
                
                secAction = MudAction.MudAction()
                
                secAction.actionType = 'vision'
                secAction.playerRef  = player
                secAction.data1      = player.zone
                secAction.data2      = player.room
                try:
                    secAction.string = player.statistics['warpout']
                except:
                    secAction.string = player.name+' vanishes in a flash of light.'
                
                MudActionHandler.actionHandler.doAction(secAction)
                MudActionHandler.actionHandler.doAction(newAction)
                
                secAction.data1 = player.zone
                secAction.data2 = player.room
                try:
                    secAction.string = player.statistics['warpin']
                except:
                    secAction.string = player.name+' appears in a flash of light.'
                
                MudActionHandler.actionHandler.doAction(secAction)
                return
        
        args = args.split(" ", 1)
        
        
        if len(args) == 1:
            t_z = player.zone
            t_r = int(args[0])
        
        elif len(args) == 2:
            t_z = int(args[0])
            t_r = int(args[1])
        
        else:
            player.writeWithPrompt("Proper format is: "+self.useExample)
            return
        
        newAction = MudAction.MudAction()
        newAction.actionType = 'forcetransport'
        newAction.playerRef  = player
        newAction.data1      = t_z
        newAction.data2      = t_r
        
        secAction = MudAction.MudAction()
        
        secAction.actionType = 'vision'
        secAction.playerRef  = player
        secAction.data1      = player.zone
        secAction.data2      = player.room
        try:
            secAction.string = player.statistics['warpout']
        except:
            secAction.string = player.name+' vanishes in a flash of light.'
        
        MudActionHandler.actionHandler.doAction(secAction)
        MudActionHandler.actionHandler.doAction(newAction)
        
        secAction.data1 = player.zone
        secAction.data2 = player.room
        try:
            secAction.string = player.statistics['warpin']
        except:
            secAction.string = player.name+' appears in a flash of light.'
        
        MudActionHandler.actionHandler.doAction(secAction)


warp = cmdWarp()