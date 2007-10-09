"""
cmdNewTemplate.py
Author: Fletcher Haynes
This file handles creating a new character or item template.
"""

import MudCommand
import MudWorld
import MudItem
import MudCharacter

import string

class cmdNewTemplate(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "newtemplate"
        self.info['helpText']   = '''Creates a new template with the optionally specified name.'''
        self.info['useExample'] = '''newtemplate character/item Name of Template'''
        
    def process(self, player, args=''):
        argList = args.split(" ", 1)
        if len(argList) != 2:
            player.writeWithPrompt("You must specify a template type (item or character) and a name.")
            return
        
        if argList[0].lower() == 'item':
            newTemplate = MudItem.MudItem()
            newTemplate.setId(MudWorld.world.idDb.getNewId('itemtemplate'))
            newTemplate.setName(argList[1])
            MudWorld.world.templateDb.addTemplate('item', newTemplate)
            MudWorld.world.db.saveIdDatabase()
            MudWorld.world.db.saveTemplateDatabase()
            player.writeWithPrompt("Item Template: "+argList[1]+" created with an ID of: "+str(newTemplate.getId())+".")

        elif argList[0].lower() == 'character':
            newTemplate = MudCharacter.MudCharacter()
            newTemplate.setId(MudWorld.world.idDb.getNewId('chartemplate'))
            newTemplate.setName(argList[1])
            MudWorld.world.templateDb.addTemplate('character', newTemplate)
            MudWorld.world.db.saveIdDatabase()
            MudWorld.world.db.saveTemplateDatabase()
            player.writeWithPrompt("Character Template: "+argList[1]+" created ith an ID of: "+str(newTemplate.getId())+".")

        else:
            player.writeWithPrompt("You specified an invalid template type. Please use item or character.")
            return


        
