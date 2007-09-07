import MudPortal
import MudCommand
import MudDatabase
import MudConst

class cmdPromote(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "promote"
        self.helpText   = '''This lets you promote a person to immortal status.'''
        self.useExample = '''promote Kuros enforcer/builder/scripter/implementor'''


    def Process(self, player, args=''):
        args = args.split(" ", 1)
        if len(args) != 2:
            player.writeWithPrompt("Proper format is: promote Kuros level!")
            return
        
        if MudDatabase.db.findCharByName(args[0]):
            tmp = MudDatabase.db.findCharByName(args[0])
            if args[1].lower() == 'builder':
                MudDatabase.db.loadBuilderCmds(MudDatabase.db.findCharByName(args[0]))
                tmp.admin_level = MudConst.builder
                player.writeWithPrompt("Done!")
                tmp.writeWithPrompt("You have been promoted to: Builder!")
                return
            elif args[1].lower() == 'implementor':
                MudDatabase.db.loadAllCmds(MudDatabase.db.findCharByName(args[0]))
                tmp.admin_level = MudConst.implementor
                player.writeWithPrompt("Done!")
                tmp.writeWithPrompt("You have been promoted to: Implementor!")
                return
            else:
                player.writeWithPrompt("Not a valid promotion level!")
                return


promote = cmdPromote()