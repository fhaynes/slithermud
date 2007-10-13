"""
cmdInfo.py
Author: Fletcher Haynes
This command allows the user to see detailed information about a template,
instance, room, or portal.
"""

import MudCommand
import MudWorld
import columnize
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
                player.writeWithPrompt("That character instance was not found.")
                return
            
            player.writePlain("<red>[Name]: <r> "+t.getName()+'\r\n')
            player.writePlain("<red>[ID  ]: <r>"+str(t.getId())+'\r\n')
            player.writePlain("<red>[TID ]: <r>"+str(t.getTemplateId())+'\r\n')
            player.writePlain("\r\n<green>[STATISTICS]")
            statList = t.getStats().keys()
            newList = []
            for eachItem in statList:
                eachItem = eachItem + ": "+str(t.getStat(eachItem))
                newList.append(eachItem)
            columnize.columnize(player,  newList, 4)
            cmdList = t.getCommands()
            player.writePlain("\r\n\r\n<green>[COMMANDS]<r>")
            columnize.columnize(player, cmdList, 6)
            player.writePlain('\r\n\r\n<green>[LOGICS]<r>')
            logicList = t.getLogics().keys()
            columnize.columnize(player, logicList, 6)
            player.writeWithPrompt("\r\nEND INFO")
            
            
            
            
        elif argList[0].lower() == 'ctemplate':
            
            t = MudWorld.world.templateDb.findTemplateById('character', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
            player.writePlain("<red>[Name]: <r> "+t.getName()+'\r\n')
            player.writePlain("<red>[ID  ]: <r>"+str(t.getId())+'\r\n')
            player.writePlain("\r\n<green>[STATISTICS]")
            statList = t.getStats().keys()
            for eachItem in statList:
                eachItem = eachItem + ": "+str(t.getStat(eachItem))
            columnize.columnize(player,  statList, 4)
            cmdList = t.getCommands()
            player.writePlain("\r\n\r\n<green>[COMMANDS]<r>")
            columnize.columnize(player, cmdList, 6)
            player.writePlain('\r\n\r\n<green>[LOGICS]<r>')
            logicList = t.getLogics().keys()
            columnize.columnize(player, logicList, 6)
            player.writeWithPrompt("\r\nEND INFO")
                    
        elif argList[0].lower() == 'itemplate':
            t = MudWorld.world.templateDb.findTemplateById('item', int(argList[1]))
            if t == None:
                player.writeWithPrompt("That template was not found.")
                
            player.writePlain("<red>[Name]: <r> "+t.getName()+'\r\n')
            player.writePlain("<red>[ID  ]: <r>"+str(t.getId())+'\r\n')
            player.writePlain("\r\n<green>[STATISTICS]")
            statList = t.getStats().keys()
            for eachItem in statList:
                eachItem = eachItem + ": "+str(t.getStat(eachItem))
            columnize.columnize(player,  statList, 4)
            cmdList = t.getCommands()
            player.writePlain("\r\n\r\n<green>[COMMANDS]<r>")
            columnize.columnize(player, cmdList, 6)
            player.writePlain('\r\n\r\n<green>[LOGICS]<r>')
            logicList = t.getLogics().keys()
            columnize.columnize(player, logicList, 6)
            player.writeWithPrompt("\r\nEND INFO")
            
                
                    
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
            player.writePlain("<red>[Name]: <r> "+t.getName()+'\r\n')
            player.writePlain("<red>[ID  ]: <r>"+str(t.getId())+'\r\n')
            player.writePlain("<red>[TID ]: <r>"+str(t.getTemplateId())+'\r\n')
            player.writePlain("\r\n<green>[STATISTICS]")
            statList = t.getStats().keys()
            for eachItem in statList:
                eachItem = eachItem + ": "+str(t.getStat(eachItem))
            columnize.columnize(player,  statList, 4)
            cmdList = t.getCommands()
            player.writePlain("\r\n\r\n<green>[COMMANDS]<r>")
            columnize.columnize(player, cmdList, 6)
            player.writePlain('\r\n\r\n<green>[LOGICS]<r>')
            logicList = t.getLogics().keys()
            columnize.columnize(player, logicList, 6)
            player.writeWithPrompt("\r\nEND INFO")

            
            player.writeWithPrompt(argList[2]+' was changed to: '+str(argList[3])+' on: '+t.getName())
        else:
            player.writeWithPrompt("Invalid type. Please use iinstance, itemplate, cinstance, or ctemplate.")
            return
        
        

