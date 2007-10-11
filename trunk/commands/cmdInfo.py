"""
cmdInfo.py
Author: Fletcher Haynes
This command allows the user to see detailed information about a template,
instance, room, or portal.
"""

import MudCommand
import MudWorld

import string
import os

class cmdInfo(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "info"
        self.info['helpText']   = '''Displays detailed informatin about a template, instance, room or portal.'''
        self.info['useExample'] = "info ctemplate/cinstance/itemplate/iinstance ID"
        
    def process(self, player, args=''):
        argList = args.split(" ", 1)
        t = None
        if len(argList) != 2:
            player.writeWithPrompt("Proper format is: info ctemplate/cinstance/itemplate/iinstance ID")
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

            player.writePlain("Name: "+t.getName()+'\r\n')
            player.writePlain("ID  : "+str(t.getId())+'\r\n')
            
                    
            
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
            
        elif argList[0].lower() == 'ctemplate':
            
            t = MudWorld.world.templateDb.findTemplateById('character', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            if argList[3].isdigit():
                if t.hasStat(argList[2]):
                    t.setStat(argList[2], int(argList[3]))
                    return
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
            else:
                if t.hasStat(argList[2]):
                    t.info[argList[2]] = argList[3]
                    return
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
                    
        elif argList[0].lower() == 'itemplate':
            t = MudWorld.world.templateDb.findTemplateById('item', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            if argList[3].isdigit():
                if t.hasStat(argList[2]):
                    t.setStat(argList[2], int(argList[3]))
                    return
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
            else:
                if t.hasStat(argList[2]):
                    t.info[argList[2]] = argList[3]
                    return
                else:
                    player.writeWithPrompt("That template does not have that stat. Please use addstat to add it.")
                    return
                    
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
                    return
                else:
                    player.writeWithPrompt("That item does not have that stat. Please use addstat to add it.")
                    return
                    
            
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
        else:
            player.writeWithPrompt("Invalid type. Please use iinstance, itemplate, cinstance, or ctemplate.")
            return
        
        

