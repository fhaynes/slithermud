import MudCommand
import MudAction
import MudActionHandler
import autoreload
class cmdInventory(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName  = "inventory"
        self.helpText = '''This displays the contents of your inventory.'''
        self.useExample = 'inventory'

    def Process(self, player, args=''):
        player.writePlain('\r\n<green>INVENTORY CONTENTS:\r\n<r>')
        for eachThing in player.items.values():
            player.writePlain('<cyan>'+eachThing.name+'\r\n<r>')
        player.writeWithPrompt("")

    




inventory = cmdInventory()