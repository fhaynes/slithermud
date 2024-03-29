"""
cmdEdit.py
Author: Fletcher Haynes
This command allows editing of instance and template attributes.
"""

import MudCommand
import MudWorld

import string
import os

class cmdEdit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "edit"
        self.info['helpText']   = '''Lets you edit template and instance attributes.'''
        self.info['useExample'] = "edit cinstance/ctemplate/iinstance/itemplate \
        ID field value"
        
    def process(self, player, args=''):
        argList = args.split(" ", 3)
        t = None
        if len(argList) != 4:
            player.writeWithPrompt("Proper format is: edit type id field value.")
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

            if argList[3].isdigit():
                if t.hasStat(argList[2]):
                    t.setStat(argList[2], int(argList[3]))
                else:
                    player.writeWithPrompt("That object does not have that stat.")
                    return
            else:
                if t.hasStat(argList[2]):
                    t.info[argList[2]] = argList[3]
                else:
                    player.writeWithPrompt("That object does not have that stat.")
                    return
                    
            
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
            
        elif argList[0].lower() == 'ctemplate':
            
            t = MudWorld.world.templateDb.findTemplateById('character', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
            
            if argList[2].lower() == 'addlogic':
                name, logic = MudWorld.world.logicDb.getLogic(argList[3])
                t.addLogic(name, logic)
                player.writeWithPrompt("Logic module: "+name+" added.")
                return
            
            if argList[2].lower() == 'dellogic':
                try:
                    t.removeLogic(argList[3])
                except:
                    player.writeWithPrompt("The template does not have logic module: "+argList[3])
                    return
                
            if argList[3].isdigit():
                if t.hasStat(argList[2]):
                    t.setStat(argList[2], int(argList[3]))
                    MudWorld.world.db.saveTemplateDatabase()
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
            else:
                if t.hasStat(argList[2]):
                    t.info[argList[2]] = argList[3]
                    MudWorld.world.db.saveTemplateDatabase()
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
                    
        elif argList[0].lower() == 'itemplate':
            t = MudWorld.world.templateDb.findTemplateById('item', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            if argList[3].isdigit():
                if t.hasStat(argList[2]):
                    t.setStat(argList[2], int(argList[3]))
                    MudWorld.world.db.saveTemplateDatabase()
                    
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
            else:
                if t.hasStat(argList[2]):
                    t.info[argList[2]] = argList[3]
                    MudWorld.world.db.saveTemplateDatabase()
                    
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
                    
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
            if argList[3].isdigit():
                if t.hasStat(argList[2]):
                    t.setStat(argList[2], int(argList[3]))
                    return
                else:
                    player.writeWithPrompt("That item does not have that stat. Please use addstat to add it.")
                    return
            else:
                if t.hasStat(argList[2]):
                    t.info[argList[2]] = argList[3]
                else:
                    player.writeWithPrompt("That item does not have that stat. Please use addstat to add it.")
                    return
                    
            
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
        else:
            player.writeWithPrompt("Invalid type. Please use iinstance, itemplate, cinstance, or ctemplate.")
            return
        
        

