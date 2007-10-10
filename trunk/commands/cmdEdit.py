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

            if t.getInfo().has_key(argList[2]):
                if argList[3].isdigit():
                    t.info[argList[2]] = int(argList[3])
                    return
                else:
                    t.info[argList[2]] = argList[3]
                    return
                    
            else:
                player.writeWithPrompt("The character does not have that attribute.")
                return
            
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
            
        elif argList[0].lower() == 'ctemplate':
            pass
        elif argList[0].lower() == 'itemplate':
            pass
        elif argList[0].lower() == 'iinstance':
            pass
        else:
            player.writeWithPrompt("Invalid type. Please use iinstance, itemplate, cinstance, or ctemplate.")
            return
        
        

