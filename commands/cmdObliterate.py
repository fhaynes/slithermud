"""
cmdObliterate.py
Author: Fletcher Haynes
This commands deletes an instance or template from the game.
"""

import MudCommand
import MudWorld
import MudAction
import string

class cmdObliterate(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "obliterate"
        self.info['helpText']   = '''Destroys a template or ID.'''
        self.info['useExample'] = '''obliterate iinstance/itemplate/cinstance/ctemplate ID'''
        
    def process(self, player, args=''):
        argList = args.split(" ", 1)
        t = None
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is: obliterate type ID.")
            return
        
        if argList[0].lower() == 'cinstance':
            for eachChar in player.getRoomRef().getCharacters().values():
                try:
                    if eachChar.getId() == int(argList[1]):
                        t = eachChar
                        break
                except:
                    player.writeWithPrompt("IDs must be numbers only!")
                    return
            
            if t == None:
                player.writeWithPrompt("A character with that ID was not found in this room.")
                return
            
            newAction = MudAction.MudAction('destroycharacter', player, t)
            MudWorld.world.actionHandler.doAction(newAction)
            player.writeWithPrompt("Character instance: "+t.getName()+' was deleted.')
            

            
        elif argList[0].lower() == 'ctemplate':
            
            t = MudWorld.world.templateDb.findTemplateById('character', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            MudWorld.world.templateDb.removeTemplate('character', t.getId())
            player.writeWithPrompt("Template: "+t.getName()+" was deleted.")
                
                    
        elif argList[0].lower() == 'itemplate':
            t = MudWorld.world.templateDb.findTemplateById('item', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")

            MudWorld.world.templateDb.removeTemplate('item', t.getId())
            player.writeWithPrompt("Template: "+t.getName()+" was deleted.")
                    
        elif argList[0].lower() == 'iinstance':
            for eachItem in player.getRoomRef().getItems().values():
                try:
                    if eachItem.getId() == int(argList[1]):
                        t = eachItem
                        break
                except:
                    player.writeWithPrompt("IDs must be numbers only!")
                    return
            if t == None:
                player.writeWithPrompt("An item with that ID was not found in this room.")
                return
            newAction = MudAction.MudAction('destroyitem', player, t)
            MudWorld.world.actionHandler.doAction(newAction)
            player.writeWithPrompt("Item instance: "+t.getName()+' was deleted.')
            
        else:
            player.writeWithPrompt("Invalid type. Please use iinstance, itemplate, cinstance, or ctemplate.")
            return