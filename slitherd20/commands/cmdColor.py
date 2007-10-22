import MudCommand

class cmdColor(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "color"
        self.info['helpText']   = '''Lets you toggle color on or off.'''
        self.info['useExample'] = '''color on/off'''
        
    def process(self, player, args=''):
        if args.lower() == 'on':
            player.setColor(True)
            player.writeWithPrompt("Color is now ON.")
        elif args.lower() == 'off':
            player.setColor(False)
            player.writeWithPrompt("Color is now OFF.")
        else:
            player.writeWithPrompt("Please specify on or off.")
            return