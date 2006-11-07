"""
The OLC Manager

@author: Fletcher Haynes
@copyright: (c)2006 Fletcher Haynes, All rights reserved.
"""

import textwrap
import os
import sys

import MudWorld
import MudRoom
import MudZone
import MudConst
import MudPortal
import MudCharacter
import MudDatabase
import MudItem

class OlcManager:
    def __init__(self):
        
        self.users = []
        self.cur_zones = MudDatabase.db.zones
        
        
        # OLC states - states the user can be in while using the OLC
        
        # Initial and Zone Editing States
        self.initialMenu      = 0
        self.zoneEditPage     = 1
        self.zoneSelectPage   = 2
        self.roomSelectPage   = 3
        self.roomEditPage     = 4
        self.portalEditPage   = 6
        self.mobSelectPage    = 7
        self.mobEditPage      = 8
        self.itemSelectPage   = 9
        self.itemEditPage     = 10
        
    def addUser(self, user):
        self.users.append(user)
        user.olcState = 0
        user.curWorkingPortal       = None
        user.curWorkingRoom         = None
        user.curWorkingItemTemplate = None
        user.curWorkingCharTemplate = None
        user.curWorkingZone         = None
        self.displayMainMenu(user)
        
    def removeUser(self, user):
        self.users.remove(user)
        del user.curWorkingPortal
        del user.curWorkingRoom
        del user.curWorkingItemTemplate
        del user.curWorkingZone
        
    def handleInput(self, user, args):
        if args.lower() == 'save zone':
            MudDatabase.db.saveZoneToDisk(user.curWorkingZone)
            user.writePlain('Zone saved!\r\n>> ')
            return
        elif args.lower() == 'save ctemplate':
            if user.curWorkingCharTemplate != None:
                MudDatabase.db.saveCharTemplateToDisk(user.curWorkingCharTemplate)
                user.writePlain('Template saved!\r\n>> ')
                return
            else:
                user.writePlain('You do not have an active template!\r\n>> ')
                return
        elif args.lower() == 'save itemplate':
            if user.curWorkingItemTemplate != None:
                MudDatabase.db.saveItemTemplateToDisk(user.curWorkingItemTemplate)
                user.writePlain('Template saved!\r\n>> ')
                return
            else:
                user.writePlain('You do not have an active template!\r\n>> ')
                return
            
        elif args.lower() == 'quit':
            user.writePlain('Exiting OLC System!\r\n')
            self.removeUser(user)
            user.login_state = MudConst.logedIn
            user.writeWithPrompt("<cls>")
            user.curWorkingZone = None
            user.curWorkingRoom = None
            user.curWorkingPortal = None
        # Initial menu and zone editing function calls
        elif user.olcState == self.initialMenu:
            self.initialMenuProcess(user, args)
        elif user.olcState == self.zoneEditPage:
            self.zoneEditProcess(user, args)
        elif user.olcState == self.zoneSelectPage:
            self.zoneSelectProcess(user, args)
        elif user.olcState == self.roomSelectPage:
            self.roomSelectProcess(user, args)
        elif user.olcState == self.roomEditPage:
            self.roomEditProcess(user, args)
        elif user.olcState == self.portalEditPage:
            self.portalEditProcess(user, args)
        elif user.olcState == self.mobSelectPage:
            self.mobSelectProcess(user, args)
        elif user.olcState == self.mobEditPage:
            self.mobEditProcess(user, args)
        elif user.olcState == self.itemSelectPage:
            self.itemSelectProcess(user, args)
        elif user.olcState == self.itemEditPage:
            self.itemEditProcess(user, args)
        else:
            pass 
    def initialMenuProcess(self, user, args):
        if args.lower() == 'n':
            user.curWorkingZone = self.createNewZone(user)
            user.writePlain('Zone created! Taking you to the Editing Page.\r\n')
            user.olcState = self.zoneEditPage
            self.displayZoneEditPage(user)
        elif args.lower() == 'l':
            self.displayZoneListPage(user)
            user.olcState = self.zoneSelectPage
        elif args.lower() == 't':
            self.displayMobSelectPage(user)
            user.olcState = self.mobSelectPage
        elif args.lower() == 'i':
            self.displayItemSelectPage(user)
            user.olcState = self.itemSelectPage
        else:
            user.writePlain('\r\n>> ')
            
        
        
    def displayMainMenu(self, user):
        user.writePlain('<cls><bright><white>SlitherMUD OLC Main Menu\r\n')
        user.writePlain('<bright><white>\r\n\r\n----------Main Menu----------\r\n')
        user.writePlain('     \r\n     <red>[N]ew Zone\r\n')
        user.writePlain('     [L]ist Existing Zones\r\n')
        user.writePlain('     [T]emplate Editing for Character\r\n')
        user.writePlain('     [I]tem Template Editing\r\n')
        user.writePlain('     [Quit] the OLC Editor\r\n<white>')
        user.writePlain('\r\n-----------------------------\r\n')
        user.writePlain('\r\n<r>>> ')
        
    def zoneSelectProcess(self, user, args):
        if args.isdigit():
            try:
                user.curWorkingZone = self.cur_zones[int(args)]
                user.olcState = self.zoneEditPage
                self.displayZoneEditPage(user)
            except KeyError:
                user.writePlain('\r\nThat is not a valid Zone ID. Try again: ')
        elif args == '':
            self.displayZoneListPage(user)
        elif args == 'back':
            user.olcState = self.initialMenu
            self.displayMainMenu(user)
        else:
            user.writePlain('Zone IDs must be numbers only. Try again: ')
            
    def zoneEditProcess(self, user, args):
        args = args.split(" ", 1)
        try:
            if args[0].lower() == 'name':
                user.curWorkingZone.name = args[1]
                self.displayZoneEditPage(user)
                return
            elif args[0] == '':
                self.displayZoneEditPage(user)
            elif args[0].lower() == 'back':
                user.olcState = self.zoneSelectPage
                self.displayZoneListPage(user)
            elif args[0].lower() == 'id':
                if args[1].isdigit():
                    if self.cur_zones.has_key(int(args[1])):
                        user.writePlain('That ID is already taken!\r\n>> ')
                        return
                    user.curWorkingZone.id_num = int(args[1])
                    self.displayZoneEditPage(user)
                    return
                else:
                    user.writePlain('Zone ID must be numerical.\r\n>> ')
                    return
            elif args[0].lower() == 'permissions':
                for eachUser in user.curWorkingZone.permissions:
                    if args[1].lower() == eachUser.lower():
                        user.curWorkingZone.permissions.remove(eachUser)
                        self.displayZoneEditPage(user)
                        return
                user.curWorkingZone.permissions.append(args[1].capitalize)
                self.displayZoneEditPage(user)
                return
            elif args[0].lower() == 'logics':
                if len(args[1].split(" ")) != 1:
                    user.writePlain('Proper format is logics modulename. No spaces.')
                    user.writePlain('\r\n>> ')
                    return
                if user.curWorkingZone.logic_modules.has_key(args[1]):
                    del user.curWorkingZone.logic_modules[args[1]]
                    self.displayZoneEditPage(user)
                    return
                else:
                    try:
                        user.curWorkingZone.logic_modules[args[1]] = __import__(args[1])
                        user.writePlain('Logic module added!\r\n\r\n>>')
                        return
                    except:
                        user.writePlain('Cannot find that logic module!\r\n>>')
                        return
            elif args[0].lower() == 'roomedit':
                user.olcState = self.roomSelectPage
                self.displayRoomListPage(user)
            else:
                user.writePlain('That is not a valid option.\r\n>> ')
        except:
            user.writePlain('Invalid command.\r\n>> ')
        
    def roomSelectProcess(self, user, args):
        args = args.split(" ", 1)
        if args[0].lower() == 'edit':
            if not args[1].isdigit():
                user.writePlain('Room to edit must be numbers only! Format is edit idnum.\r\n')
                user.writePlain('>> ')
                return
            try:
                user.curWorkingRoom = user.curWorkingZone.rooms[int(args[1])]
                user.olcState = self.roomEditPage
                self.displayRoomEditPage(user)
            except:
                
                newRoom = MudRoom.MudRoom()
                newRoom.zone = user.curWorkingZone.id_num
                newRoom.name = 'NoName'
                newRoom.desc = 'Empty'
                newRoom.id_num = int(args[1])
                newRoom.addLogic('basicRoomLogic')
                user.curWorkingRoom = newRoom
                user.curWorkingZone.addRoom(newRoom)
                user.olcState = self.roomEditPage
                self.displayRoomEditPage(user)
        elif args[0] == '':
            self.displayRoomListPage(user)
        elif args[0].lower() == 'back':
            user.olcState = self.zoneEditPage
            self.displayZoneEditPage(user)
                
        else:
            user.writePlain('Invalid command.\r\n>>')
            
    def roomEditProcess(self, user, args):
        args = args.split(" ", 1)
        if args[0].lower() == 'name':
            if args[0].isalpha():
                user.curWorkingRoom.name = args[1]
                self.displayRoomEditPage(user)
                
            else:
                user.writePlain('Room names can only have letters!')
                user.writePlain('\r\n>> ')
                return
        elif args[0].lower() == 'pedit':
            if len(args) != 2:
                user.writePlain("Proper format is: pedit idnum!\r\n>>")
                return
            if not args[1].isdigit():
                user.writePlain("ID Numbers must be numbers!\r\n>>")
                return
            if user.curWorkingRoom.portals.has_key(int(args[1])):
                user.curWorkingPortal = user.curWorkingRoom.portals[int(args[1])]
                user.olcState = self.portalEditPage
                self.displayPortalEditPage(user)
            else:
                newPortal = MudPortal.MudPortal()
                newPortal.zone = user.curWorkingZone.id_num
                newPortal.name = 'NoName'
                newPortal.desc = 'Empty'
                newPortal.anchor = int(user.curWorkingRoom.id_num)
                newPortal.id_num = int(args[1])
                newPortal.target_zone = user.curWorkingZone.id_num
                newPortal.addLogic('basicPortalLogic')
                user.curWorkingPortal = newPortal
                user.curWorkingRoom.addPortal(newPortal)
                user.olcState = self.portalEditPage
                self.displayPortalEditPage(user)
                
        elif args[0].lower() == 'logics':
            if len(args[1].split(" ")) != 1:
                user.writePlain('Proper format is logics modulename. No spaces.')
                user.writePlain('\r\n>> ')
                return
            if user.curWorkingRoom.logic_modules.has_key(args[1]):
                del user.curWorkingRoom.logic_modules[args[1]]
                self.displayRoomEditPage(user)
                return
            else:
                try:
                    user.curWorkingRoom.logic_modules[args[1]] = __import__(args[1])
                    user.writePlain('Logic module added!\r\n\r\n>>')
                    return
                except:
                    user.writePlain('Cannot find that logic module!\r\n>>')
                    return
        elif args[0].lower() == 'id':
            if args[1].isdigit():
                if user.curWorkingZone.rooms.has_key(int(args[1])):
                    user.writePlain('That ID is already assigned to a room.')
                    user.writePlain('\r\n>> ')
                else:
                    user.curWorkingRoom.id_num = int(args[1])
            else:
                user.writePlain('ID Numbers must be numbers only.')
                user.writePlain('\r\n>> ')
                
        elif args[0].lower() == 'desc':
            user.curWorkingRoom.desc = ''
            try:
                if args[1] == 'end':
                    user.curWorkingRoom.desc = user.buffer
                    user.buffer = ''
                else:
                    user.buffer = user.buffer + args[1]+' '
            except IndexError:
                user.writePlain("You must type something to add to the desc!\r\n>>")
                return
        elif args[0] == '':
            self.displayRoomEditPage(user)
        elif args[0].lower() == 'back':
            user.olcState = self.roomSelectPage
            self.displayRoomListPage(user) 
        else:
            pass

    def portalEditProcess(self, user, args):
        args = args.split(" ", 1)
        if args[0].lower() == 'name':
            if args[1].isalpha():
                user.curWorkingPortal.name = args[1]
                self.displayPortalEditPage(user)
                return
            else:
                user.writePlain('Portal names cannot contain numbers.')
                user.writePlain('\r\n >>')
                return
        elif args[0].lower() == 'id':
            if args[1].isdigit():
                user.curWorkingPortal.id_num = int(args[1])
                self.displayPortalEditPage(user)
                return
            else:
                user.writePlain('Portal IDs must be numbers only.')
                user.writePlain('\r\n >>')
                return
        elif args[0].lower() == 'targetr':
            if args[1].isdigit():
                user.curWorkingPortal.target_room = int(args[1])
                self.displayPortalEditPage(user)
                return
            else:
                user.writePlain('Portal Targets must be the ID of the room they lead too.')
                user.writePlain('\r\n>> ')
                return
        elif args[0].lower() == 'targetz':
            if args[1].isdigit():
                user.curWorkingPortal.target_zone = int(args[1])
                self.displayPortalEditPage(user)
                return
            else:
                user.writePlain('Portal Targets must be the ID of the room they lead too.')
                user.writePlain('\r\n>> ')
                return
        elif args[0].lower() == 'logics':
                if len(args[1].split(" ")) != 1:
                    user.writePlain('Proper format is logics modulename. No spaces.')
                    user.writePlain('\r\n>> ')
                    return
                if user.curWorkingPortal.logic_modules.has_key(args[1]):
                    del user.curWorkingPortal.logic_modules[args[1]]
                    self.displayPortalEditPage(user)
                    return
                else:
                    try:
                        user.curWorkingPortal.logic_modules[args[1]] = __import__(args[1])
                        user.writePlain('Logic module added!\r\n\r\n>>')
                        return
                    except:
                        user.writePlain('Cannot find that logic module!\r\n>>')
                        return
        elif args[0] == '':
            self.displayPortalEditPage(user)
        elif args[0].lower() == 'back':
            user.olcState = self.roomEditPage
            self.displayRoomEditPage(user) 
        
        else:
            user.writePlain('Invalid command. \r\n>> ')
            
    def mobSelectProcess(self, user, args):
        args = args.split(" ")
        if args[0].lower() == 'search':
            if len(args) < 2:
                user.writePlain("You must search for something!\r\n>> ")
                return
            args[1] = args[1].replace(" ", "")
            x = 0
            y = 0
            for eachTemp in MudDatabase.db.c_templates.values():
                if eachTemp.name.lower().search(args[1].lower()):
                    x = x + 1
                    y = y + 1
                    if x == 3:
                        user.writePlain('['+str(eachTemp.id_num)+'] ['+eachTmp.name+']\r\n')
                        x = 0
                    else:
                        user.writePlain('['+str(eachTemp.id_num)+'] ['+eachTmp.name+']\r\n')
            if y != 0:
                user.writePlain('>> ')
                return
            else:
                user.writePlain('Could not find any templates matching that parameter!\r\n>> ')
                return
            
        elif args[0].lower() == 'edit':
            try:
                if not int(args[1]) in range(user.statistics['m_lvnum'], user.statistics['m_hvnum']):
                    user.writePlain("That ID number is not within your assigned range!\r\n>>")
                    return
            except IndexError:
                user.writePlain("Edit what ID?\r\n>>")
                return
            try:
                user.curWorkingCharTemplate = MudDatabase.db.c_templates[int(args[1])]
                user.olcState = self.mobEditPage
                self.displayMobEditPage(user)
            except:
                print "Doh!"
                newTemplate = MudCharacter.MudCharacterTemplate()
                newTemplate.id_num = int(args[1])
                newTemplate.statistics['str'] = 1
                newTemplate.statistics['int'] = 1
                newTemplate.statistics['dex'] = 1
                newTemplate.statistics['sta'] = 1
                newTemplate.statistics['spi'] = 1
                newTemplate.logics.append('basicCharLogic')
                user.curWorkingCharTemplate = newTemplate
                user.olcState = self.mobEditPage
                self.displayMobEditPage(user)
        else:
            self.displayMobSelectPage(user)
            
    def mobEditProcess(self, user, args):
        args = args.split(" ", 1)
        try:
            if args[0].lower() == 'name':
                user.curWorkingCharTemplate.name = args[1]
                self.displayMobEditPage(user)
                return
            elif args[0] == '':
                self.displayMobEditPage(user)
            elif args[0].lower() == 'back':
                user.olcState = self.mobSelectPage
                self.displayMobSelectPage(user)
            elif args[0].lower() == 'id':
                if args[1].isdigit():
                    if not int(args[1]) in range(user.statistics['m_lvnum'], user.statistics['m_hvnum']):
                        user.writePlain("That ID number is not within your assigned range!\r\n>>")
                        return
                    if MudWorld.world.c_templates.has_key(args[1]):
                        user.writePlain('That ID is already in use!\r\n>> ')
                        return
                    else:
                        user.curWorkingCharTemplate.id_num = int(args[1])
                        self.displayMobEditPage(user)
                        return
                else:
                   user.writePlain('Template ID must be numerical.\r\n>> ')
                   return
            elif args[0].lower() == 'desc':
                user.curWorkingCharTemplate.desc = args[1]
                self.displayMobEditPage(user)
                return
            elif args[0].lower() == 'commands':
                if args[1] in user.curWorkingCharTemplate.commands:
                    user.curWorkingCharTemplate.commands.remove(args[1])
                    self.displayMobEditPage(user)
                else:
                    user.curWorkingCharTemplate.commands.append(args[1])
                    self.displayMobEditPage(user)
            elif args[0].lower() == 'logics':
                if args[1] in user.curWorkingCharTemplate.logics:
                    user.curWorkingCharTemplate.logics.remove(args[1])
                    self.displayMobEditPage(user)
                else:
                    user.curWorkingCharTemplate.logics.append(args[1])
                    self.displayMobEditPage(user)
            elif args[0].lower() == 'stats':
                tmp = args[1].split(" ")
                if len(tmp) != 2:
                    user.writePlain('Proper format is: stats name value!\r\n>> ')
                    return
                else:
                    if user.curWorkingCharTemplate.statistics.has_key(tmp[0]):
                        del user.curWorkingCharTemplate.statistics[tmp[0]]
                        self.displayMobEditPage(user)
                    else:
                        user.curWorkingCharTemplate.statistics[tmp[0]] = tmp[1]
                        self.displayMobEditPage(user)
        except ValueError:
            user.writePlain('Fix me in MobEditProcess!\r\n>> ')
            
    def itemSelectProcess(self, user, args):
        args = args.split(" ")
        if args[0].lower() == 'search':
            if len(args) < 2:
                user.writePlain("You must search for something!\r\n>> ")
                return
            args[1] = args[1].replace(" ", "")
            x = 0
            y = 0
            for eachTemp in MudDatabase.db.i_templates.values():
                if eachTemp.name.lower().search(args[1].lower()):
                    x = x + 1
                    y = y + 1
                    if x == 3:
                        user.writePlain('['+str(eachTemp.id_num)+'] ['+eachTmp.name+']\r\n')
                        x = 0
                    else:
                        user.writePlain('['+str(eachTemp.id_num)+'] ['+eachTmp.name+']\r\n')
            if y != 0:
                user.writePlain('>> ')
                return
            else:
                user.writePlain('Could not find any templates matching that parameter!\r\n>> ')
                return
            
        elif args[0].lower() == 'edit':
            if not int(args[1]) in range(user.statistics['i_lvnum'], user.statistics['i_hvnum']):
                user.writePlain("That ID number is not within your assigned range!\r\n>>")
                return
            try:
                user.curWorkingItemTemplate = MudDatabase.db.i_templates[int(args[1])]
                user.olcState = self.itemEditPage
                self.displayItemPage(user)
            except:
                newTemplate = MudItem.MudItemTemplate()
                newTemplate.id_num = int(args[1])
                user.curWorkingItemTemplate = newTemplate
                user.olcState = self.itemEditPage
                self.displayItemEditPage(user)
        else:
            self.displayItemSelectPage(user)
    def itemEditProcess(self, user, args):
        args = args.split(" ", 1)
        try:
            if args[0].lower() == 'name':
                user.curWorkingItemTemplate.name = args[1]
                self.displayItemEditPage(user)
                return
            elif args[0] == '':
                self.displayItemEditPage(user)
            elif args[0].lower() == 'back':
                user.olcState = self.itemSelectPage
                self.displayItemSelectPage(user)
            elif args[0].lower() == 'id':
                if args[1].isdigit():
                    if not int(args[1]) in range(user.statistics['i_lvnum'], user.statistics['i_hvnum']):
                        user.writePlain("That ID number is not within your assigned range!\r\n>>")
                        return
                    if MudWorld.world.templates.has_key(args[1]):
                        user.writePlain('That ID is already in use!\r\n>> ')
                        return
                    else:
                        user.curWorkingItemTemplate.id_num = int(args[1])
                        self.displayItemEditPage(user)
                        return
                else:
                   user.writePlain('Template ID must be numerical.\r\n>> ')
                   return
            elif args[0].lower() == 'desc':
                user.curWorkingItemTemplate.desc = args[1]
                self.displayItemEditPage(user)
                return
            elif args[0].lower() == 'logics':
                if args[1] in user.curWorkingItemTemplate.logics:
                    user.curWorkingItemTemplate.logics.remove(args[1])
                    self.displayItemEditPage(user)
                else:
                    user.curWorkingItemTemplate.logics.append(args[1])
                    self.displayItemEditPage(user)
            elif args[0].lower() == 'stats':
                tmp = args[1].split(" ")
                if len(tmp) != 2:
                    user.writePlain('Proper format is: stats name value!\r\n>> ')
                    return
                else:
                    if user.curWorkingItemTemplate.statistics.has_key(tmp[0]):
                        del user.curWorkingItemTemplate[tmp[1]]
                        self.displayItemEditPage(user)
                    else:
                        user.curWorkingItemTemplate.statistics[tmp[0]] = tmp[1]
                        self.displayItemEditPage(user)
        except ValueError:
            print sys.exc_info()[1]
            user.writePlain('Fix me in MobEditProcess!\r\n>> ')
        
    def displayZoneEditPage(self, user):
        user.writePlain('<cls>Zone Creation and Editing Section\r\n\r\n')
        user.writePlain('[Name]       :  '+user.curWorkingZone.name+'\r\n')
        user.writePlain('[ID]         :  '+str(user.curWorkingZone.id_num)+'\r\n')
        y = 0
        user.writePlain('[Permissions]\r\n\r\n')
        for eachAllowed in user.curWorkingZone.allowed:
            if y == 4:
                user.writePlain('\r\n')
                y = 0
            user.writePlain(eachAllowed+'    ')
        y = 0
        user.writePlain('\r\n\r\n[Logics]\r\n')
        for eachModule in user.curWorkingZone.logic_modules.keys():
            if y == 4:
                user.writePlain('\r\n')
                y = 0
            user.writePlain(eachModule+'    ')

        user.writePlain('\r\n\r\n>> ')
    def displayZoneListPage(self, user):
        user.writePlain('<cls><bright><white>SlitherMUD OLC Main Menu\r\n\r\n')
        user.writePlain('<under><bright><white>Zone ID<r>    <under><bright><white>Zone Name<r>\r\n')
        for eachZone in self.cur_zones.keys():
            user.writePlain('\r\n'+str(eachZone)+'         '+self.cur_zones[eachZone].name+'\r\n')
        user.writePlain('>>')
        
    def displayRoomListPage(self, user):
        user.writePlain('<cls><bright><white>SlitherMUD OLC Room List Page<r>\r\n\r\n')
        user.writePlain('Rooms range from 1 to ')
        cnt = 1
        for eachRoom in user.curWorkingZone.rooms.keys():
            cnt = cnt + 1
        user.writePlain(str(cnt)+'.\r\n')
        user.writePlain('>> ')
        
    def displayRoomEditPage(self, user):
        try:
            desc = self.formatOutput(user.curWorkingRoom.desc)
            user.writePlain('<cls><white><bright>SlitherMUD OLC Room Edit Page<r>\r\n\r\n')
            user.writePlain('[Name]     : '+user.curWorkingRoom.name+'\r\n')
            user.writePlain('[ID]       : '+str(user.curWorkingRoom.id_num)+'\r\n')
            user.writePlain('[Desc]\r\n'+desc+'\r\n')
            user.writePlain('\r\n[Portals]\r\n')
            x = 0
            for eachPortal in user.curWorkingRoom.portals.keys():
                if x == 4:
                    user.writePlain('\r\n')
                    x = 0
                else:
                    user.writePlain('['+str(eachPortal)+'] '+ user.curWorkingRoom.portals[eachPortal].name+'   ')
                    x = x + 1
            x = 0
            user.writePlain('\r\n\r\n[Logics]\r\n')
            for eachLogic in user.curWorkingRoom.logic_modules.keys():
                if x == 4:
                    user.writePlain('\r\n')
                    x = 0
                else:
                    user.writePlain('['+eachLogic+'] ')
                    x = x + 1
            user.writePlain('\r\n\r\n>>')
                                
        except:
            pass
            
            
    def displayPortalEditPage(self, user):
        user.writePlain('<cls><bright><white>SlitherMUD OLC Portal Editor<r>\r\n\r\n')
        user.writePlain('[Name]     : '+user.curWorkingPortal.name+'\r\n')
        user.writePlain('[ID]       : '+str(user.curWorkingPortal.id_num)+'\r\n')
        user.writePlain('[TargetR]   : '+str(user.curWorkingPortal.target_room)+'\r\n')
        user.writePlain('[TargetZ]   : '+str(user.curWorkingPortal.target_zone)+'\r\n')
        user.writePlain('\r\n[Logics]\r\n')
        x = 0
        for eachLogic in user.curWorkingPortal.logic_modules.keys():
            if x == 4:
                user.writePlain('\r\n')
                x = 0
            else:
                user.writePlain(eachLogic+'  ')
                x = x + 1
        user.writePlain('\r\n\r\n>> ')
                
    def displayMobEditPage(self, user):
        user.writePlain('<cls><white>SlitherMUD OLC Template Edit Page\r\n\r\n')
        user.writePlain('[Name] '+user.curWorkingCharTemplate.name+'\r\n')
        user.writePlain('[ID  ] '+str(user.curWorkingCharTemplate.id_num)+'\r\n')
        user.writePlain('[Desc] '+user.curWorkingCharTemplate.desc+'\r\n')
        user.writePlain('\r\n[Commands]\r\n')
        x = 0
        for eachCommand in user.curWorkingCharTemplate.commands:
            if x == 3:
                user.writePlain(eachCommand+'\r\n')
                x = 0
            else:
                user.writePlain(eachCommand+'  ')
                x = x + 1
        x = 0
        user.writePlain('\r\n\r\n[Logics]\r\n')
        for eachLogic in user.curWorkingCharTemplate.logics:
            if x == 3:
                user.writePlain(eachLogic+'\r\n')
                x = 0
            else:
                user.writePlain(eachLogic+ '  ')
                x = x + 1
        x = 0
        user.writePlain('\r\n\r\n[Stats]\r\n')
        for eachStat in user.curWorkingCharTemplate.statistics.keys():
            if x == 3:
                user.writePlain('('+eachStat+') ('+str(user.curWorkingCharTemplate.statistics[eachStat])+')\r\n')
                x = 0
            else:
                user.writePlain('('+eachStat+') ('+str(user.curWorkingCharTemplate.statistics[eachStat])+')  ')
                x = x + 1
        user.writePlain('\r\n\r\n>> ')
            
            
    def displayMobSelectPage(self, user):
        try:
            user.writePlain('<cls><white>Welcome to the Template Editing System!\r\n')
            user.writePlain('To search for a mob template by name, type search name.\r\n')
            user.writePlain('To edit that template, type edit idnum.\r\n')
            user.writePlain('To create a new template, type new.\r\n')
            user.writePlain('To save, type save.\r\n\r\n>> <r>')
        except TypeError:
            pass
        
    def displayItemEditPage(self, user):
        user.writePlain('<cls><white>SlitherMUD OLC Template Edit Page\r\n\r\n')
        user.writePlain('[Name] '+user.curWorkingItemTemplate.name+'\r\n')
        user.writePlain('[ID  ] '+str(user.curWorkingItemTemplate.id_num)+'\r\n')
        user.writePlain('[Desc] '+user.curWorkingItemTemplate.desc+'\r\n')
        x = 0
        user.writePlain('\r\n\r\n[Logics]\r\n')
        for eachLogic in user.curWorkingItemTemplate.logics:
            if x == 3:
                user.writePlain(eachLogic+'\r\n')
                x = 0
            else:
                user.writePlain(eachLogic+ '  ')
                x = x + 1
        x = 0
        user.writePlain('\r\n\r\n[Stats]\r\n')
        for eachStat in user.curWorkingItemTemplate.statistics.keys():
            if x == 3:
                user.writePlain('('+eachStat+') ('+user.curWorkingItemTemplate.statistics[eachStat]+')\r\n')
                x = 0
            else:
                user.writePlain('('+eachStat+') ('+user.curWorkingItemTemplate.statistics[eachStat]+')  ')
                x = x + 1
        user.writePlain('\r\n\r\n>> ')
    def displayItemSelectPage(self, user):
        try:
            user.writePlain('<cls><white>Welcome to the Item Template Editing System!\r\n')
            user.writePlain('To search for a item template by name, type search name.\r\n')
            user.writePlain('To edit that template, type edit idnum.\r\n')
            user.writePlain('To create a new template, type new.\r\n>> ')
        except TypeError:
            pass
    def createNewZone(self, user):
        tmp = MudZone.MudZone()
        tmp.name = ''
        tmp.allowed.append(user.name)
        x = 0
        for eachKey in self.cur_zones.keys():
            x = x + eachKey
        tmp.id_num = x
        return tmp
    
    def formatOutput(self, data):
        res = ''
        res = textwrap.fill(data, 80)
        res = res.replace('\n', '\r\n')
        #res = res.replace(']', ']\r\n')
        res = res.lstrip()
        return res
        

            
