"""
cmdAddStat.py
Author: Fletcher Haynes
This command allows adding of statistics to instances or templates.
"""

import MudCommand
import MudWorld

import string
import os

class cmdAddStat(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "addstat"
        self.info['helpText']   = '''Lets you add stats to the template or instance.'''
        self.info['useExample'] = "addstat ctemplate/cinstance/itemplate/iinstance ID statname initialvalue"
        
    def process(self, player, args=''):
        argList = args.split(" ", 3)
        t = None
        if len(argList) != 4:
            player.writeWithPrompt("Proper format is: addstat type ID statname initialvalue")
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
                player.writeWithPrompt("That character instance was not found.")
                
            if t.hasStat(argList[2]):
                player.writeWithPrompt("The character instance already has that stat.")
                return
            else:
                if argList[3].isdigit():
                    t.addStat(argList[2], int(argList[3]))
                    
                else:
                    t.addStat(argList[2], argList[3])
                    
            player.writeWithPrompt("Stat: "+argList[2]+" was added with a value of: "+str(argList[3]))
            return
            
        elif argList[0].lower() == 'ctemplate':
            
            t = MudWorld.world.templateDb.findTemplateById('character', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            if t.hasStat(argList[2]):
                player.writeWithPrompt("The character template already has that stat.")
                return
            else:
                if argList[3].isdigit():
                    t.addStat(argList[2], int(argList[3]))
                    
                else:
                    t.addStat(argList[2], argList[3])
                    
            player.writeWithPrompt("Stat: "+argList[2]+" was added with a value of: "+str(argList[3]))
            MudWorld.world.saveTemplateDatabase()
                    

        elif argList[0].lower() == 'itemplate':
            t = MudWorld.world.templateDb.findTemplateById('item', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            if t.hasStat(argList[2]):
                player.writeWithPrompt("The item template already has that stat.")
                return
            else:
                if argList[3].isdigit():
                    t.addStat(argList[2], int(argList[3]))
                    
                else:
                    t.addStat(argList[2], argList[3])
                    
            player.writeWithPrompt("Stat: "+argList[2]+" was added with a value of: "+str(argList[3]))
            MudWorld.world.saveTemplateDatabase()
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
                player.writeWithPrompt("That item instance was not found.")
            if t.hasStat(argList[2]):
                player.writeWithPrompt("The item instance already has that stat.")
                return
            else:
                if argList[3].isdigit():
                    t.addStat(argList[2], int(argList[3]))
                    
                else:
                    t.addStat(argList[2], argList[3])
                    
            player.writeWithPrompt("Stat: "+argList[2]+" was added with a value of: "+str(argList[3]))
            return
        else:
            player.writeWithPrompt("Invalid type. Please use iinstance, itemplate, cinstance, or ctemplate.")
            return
        
        

