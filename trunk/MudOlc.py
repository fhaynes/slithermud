"""
The OLC Manager

@author: Fletcher Haynes
@copyright: (c)2006 Fletcher Haynes, All rights reserved.
"""

import textwrap
import os
import sys
import exceptions

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
        self.initialMenu            = 0
        self.zoneEditPage           = 1
        self.zoneSelectPage         = 2
        self.roomSelectPage         = 3
        self.roomEditPage           = 4
        self.portalEditPage         = 6
        self.mobSelectPage          = 7
        self.mobEditPage            = 8
        self.mobInstanceEditPage    = 9
        self.itemSelectPage         = 10
        self.itemEditPage           = 11
        self.itemInstanceEditPage   = 12
        
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
        user.curWorkingPortal       = None
        user.curWorkingRoom         = None
        user.curWorkingItemTemplate = None
        user.curWorkingZone         = None
        user.curWorkingCharInstance = None
        user.curWorkingItemInstance = None
        
    def handleInput(self, user, args):
        if args.lower() == 'save ctemplate':
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
            user.login_state      = MudConst.logedIn
            user.writeWithPrompt("<cls>")
            user.curWorkingZone   = None
            user.curWorkingRoom   = None
            user.curWorkingPortal = None
        # Initial menu and zone editing function calls
        elif user.olcState == self.initialMenu:
            self.initialMenuProcess(user, args)
        #elif user.olcState == self.zoneEditPage:
        #    self.zoneEditProcess(user, args)
        #elif user.olcState == self.zoneSelectPage:
        #    self.zoneSelectProcess(user, args)
        #elif user.olcState == self.roomSelectPage:
        #    self.roomSelectProcess(user, args)
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
        elif user.olcState == self.mobInstanceEditPage:
            self.mobInstanceEditProcess(user, args)
        elif user.olcState == self.itemInstanceEditPage:
            self.itemInstanceEditProcess(user, args)
        else:
            pass 
    def initialMenuProcess(self, user, args):
        if args.lower() == 'c':
            self.displayMobSelectPage(user)
            user.olcState = self.mobSelectPage
        elif args.lower() == 'i':
            self.displayItemSelectPage(user)
            user.olcState = self.itemSelectPage
        else:
            user.writePlain('\r\n>> ')
            
    def displayMainMenu(self, user):
        user.writePlain('<bright><white>\r\n\r\n---------<green>OLC MAIN MENU<bright><white>----------\r\n')
        user.writePlain('\r\n<red>  [C]haracter Template Editing\r\n')
        user.writePlain('  [I]tem Template Editing\r\n')
        user.writePlain('  [Quit] the OLC Editor\r\n<bright><white>')
        user.writePlain('\r\n------------<green>SLITHER<bright><white>-------------\r\n')
        user.writePlain('\r\n<r>>> ')
        
    def zoneSelectProcess(self, user, args):
        pass
        #if args.isdigit():
        #    try:
        #        user.curWorkingZone = self.cur_zones[int(args)]
        #        user.olcState = self.zoneEditPage
        #        self.displayZoneEditPage(user)
        #    except KeyError:
        #        user.writePlain('\r\nThat is not a valid Zone ID. Try again: ')
        #elif args == '':
        #    self.displayZoneListPage(user)
        #elif args == 'back':
        #    user.olcState = self.initialMenu
        #    self.displayMainMenu(user)
        #else:
        #    user.writePlain('Zone IDs must be numbers only. Try again: ')
            
    def zoneEditProcess(self, user, args):
        pass
        #args = args.split(" ", 1)
        #try:
        #    if args[0].lower() == 'name':
        #        user.curWorkingZone.name = args[1]
        #        self.displayZoneEditPage(user)
        #        return
        #    elif args[0] == '':
        #        self.displayZoneEditPage(user)
        #    elif args[0].lower() == 'back':
        #        user.olcState = self.zoneSelectPage
        #        self.displayZoneListPage(user)
        #    elif args[0].lower() == 'id':
        #        if args[1].isdigit():
        #            if self.cur_zones.has_key(int(args[1])):
        #                user.writePlain('That ID is already taken!\r\n>> ')
        #                return
        #            user.curWorkingZone.id_num = int(args[1])
        #            self.displayZoneEditPage(user)
        #            return
        #        else:
        #            user.writePlain('Zone ID must be numerical.\r\n>> ')
        #            return
        #    elif args[0].lower() == 'permissions':
        #        for eachUser in user.curWorkingZone.permissions:
        #            if args[1].lower() == eachUser.lower():
        #                user.curWorkingZone.permissions.remove(eachUser)
        #                self.displayZoneEditPage(user)
        #                return
        #        user.curWorkingZone.permissions.append(args[1].capitalize)
        #        self.displayZoneEditPage(user)
        #        return
        #    elif args[0].lower() == 'logics':
        #        if len(args[1].split(" ")) != 1:
        #            user.writePlain('Proper format is logics modulename. No spaces.')
        #            user.writePlain('\r\n>> ')
        #            return
        #        if user.curWorkingZone.logic_modules.has_key(args[1]):
        #            del user.curWorkingZone.logic_modules[args[1]]
        #            self.displayZoneEditPage(user)
        #            return
        #        else:
        #            try:
        #                user.curWorkingZone.logic_modules[args[1]] = __import__(args[1])
        #                user.writePlain('Logic module added!\r\n\r\n>>')
        #                return
        #            except:
        #                user.writePlain('Cannot find that logic module!\r\n>>')
        #                return
        #    elif args[0].lower() == 'roomedit':
        #        user.olcState = self.roomSelectPage
        #        self.displayRoomListPage(user)
        #    else:
        #        user.writePlain('That is not a valid option.\r\n>> ')
        #except:
        #    user.writePlain('Invalid command.\r\n>> ')
        
    def roomSelectProcess(self, user, args):
        pass
        #args = args.split(" ", 1)
        #if args[0].lower() == 'edit':
        #    if not args[1].isdigit():
        #        user.writePlain('Room to edit must be numbers only! Format is edit idnum.\r\n')
        #        user.writePlain('>> ')
        #        return
        #    try:
        #        user.curWorkingRoom = user.curWorkingZone.rooms[int(args[1])]
        #        user.olcState = self.roomEditPage
        #        self.displayRoomEditPage(user)
        #    except:
        #        
        #        newRoom = MudRoom.MudRoom()
        #        newRoom.zone = user.curWorkingZone.id_num
        #        newRoom.name = 'NoName'
        #        newRoom.desc = 'Empty'
        #        newRoom.id_num = int(args[1])
        #        newRoom.addLogic('basicRoomLogic')
        #        user.curWorkingRoom = newRoom
        #        user.curWorkingZone.addRoom(newRoom)
        #        user.olcState = self.roomEditPage
        #        self.displayRoomEditPage(user)
        #elif args[0] == '':
        #    self.displayRoomListPage(user)
        #elif args[0].lower() == 'back':
        #    user.olcState = self.zoneEditPage
        #    self.displayZoneEditPage(user)
        #        
        #else:
        #    user.writePlain('Invalid command.\r\n>>')
            
    def roomEditProcess(self, user, args):
        args = args.split(" ", 1)
        if args[0].lower() == 'name':
            try:
                user.curWorkingRoom.name = args[1]
                self.displayRoomEditPage(user)
            except IndexError:
                user.writePlain("You must provide a new name!\r\n>> ")
                return
    
        #elif args[0].lower() == 'pedit':
        #    if len(args) != 2:
        #        user.writePlain("Proper format is: pedit idnum!\r\n>>")
        #        return
        #    if not args[1].isdigit():
        #        user.writePlain("ID Numbers must be numbers!\r\n>>")
        #        return
        #    if user.curWorkingRoom.portals.has_key(int(args[1])):
        #        user.curWorkingPortal = user.curWorkingRoom.portals[int(args[1])]
        #        user.olcState = self.portalEditPage
        #        self.displayPortalEditPage(user)
        #    else:
        #        newPortal = MudPortal.MudPortal()
        #        newPortal.zone = user.curWorkingZone.id_num
        #        newPortal.name = 'NoName'
        #        newPortal.desc = 'Empty'
        #        newPortal.anchor = int(user.curWorkingRoom.id_num)
        #        newPortal.id_num = int(args[1])
        #        newPortal.target_zone = user.curWorkingZone.id_num
        #        newPortal.addLogic('basicPortalLogic')
        #        user.curWorkingPortal = newPortal
        #        user.curWorkingRoom.addPortal(newPortal)
        #        user.olcState = self.portalEditPage
        #        self.displayPortalEditPage(user)
                
        elif args[0].lower() == 'logics':
            try:
                if len(args[1].split(" ")) != 1:
                    user.writePlain('Proper format is logics <modulename>. No spaces.')
                    user.writePlain('\r\n>> ')
                    return
                if user.curWorkingRoom.logic_modules.has_key(args[1]):
                    del user.curWorkingRoom.logic_modules[args[1]]
                    self.displayRoomEditPage(user)
                    return
                else:
                    try:
                        user.curWorkingRoom.logic_modules[args[1]] = __import__(args[1])
                        user.writePlain('Logic module added!\r\n\r\n>> ')
                        return
                    except:
                        user.writePlain('Cannot find that logic module!\r\n>> ')
                        return
            except IndexError:
                user.writePlain("You must provide a logic module name!\r\n>> ")
                return
                
                
        #elif args[0].lower() == 'id':
        #    if args[1].isdigit():
        #        if user.curWorkingZone.rooms.has_key(int(args[1])):
        #            user.writePlain('That ID is already assigned to a room.')
        #            user.writePlain('\r\n>> ')
        #        else:
        #            user.curWorkingRoom.id_num = int(args[1])
        #    else:
        #        user.writePlain('ID Numbers must be numbers only.')
        #        user.writePlain('\r\n>> ')
                
        elif args[0].lower() == 'desc':
            try:
                if args[1].lower() == 'clear':
                    user.curWorkingRoom.desc = ''
                    self.displayRoomEditPage(user)
                else:
                    user.curWorkingRoom.desc += ' '+args[1]
            except IndexError:
                user.writePlain("You must provide a new description, or type 'desc clear' to clear it!\r\n>> ")
                return
        elif args[0] == '':
            self.displayRoomEditPage(user)
        elif args[0].lower() == 'help':
            user.writePlain("This is the room editing page. Anything in []'s can be edited.\r\n")
            user.writePlain("For example, to edit the name, type name New Room Name.\r\n")
            user.writePlain("Portals cannot be edited from here. Use the newportal and edit command from the game.\r\n")
            user.writePlain("To clear a room description, type desc clear.\r\n")
            user.writePlain("When you are done, type quit. Changes are saved automatically.\r\n>> ")
        
        else:
            user.writePlain("Invalid choice! Type help for help!\r\n>> ")

    def portalEditProcess(self, user, args):
        args = args.split(" ", 1)
        if args[0].lower() == 'name':
            try:
                if args[1].isalpha():
                    user.curWorkingPortal.name = args[1]
                    self.displayPortalEditPage(user)
                    return
                else:
                    user.writePlain('Portal names cannot contain numbers.')
                    user.writePlain('\r\n >>')
                    return
            except IndexError:
                user.writePlain("You must specify a name!")
                return
                
        elif args[0].lower() == 'targetr':
            try:
                if args[1].isdigit():
                    user.curWorkingPortal.target_room = int(args[1])
                    self.displayPortalEditPage(user)
                    return
                else:
                    user.writePlain('Portal Targets must be the ID of the room they lead too.')
                    user.writePlain('\r\n>> ')
                    return
            except IndexError:
                user.writePlain("You must specify a target room!")
                return
            
        elif args[0].lower() == 'targetz':
            try:
                if args[1].isdigit():
                    user.curWorkingPortal.target_zone = int(args[1])
                    self.displayPortalEditPage(user)
                    return
                else:
                    user.writePlain('Portal Targets must be the ID of the room they lead too.')
                    user.writePlain('\r\n>> ')
                    return
            except IndexError:
                user.writePlain("You must specify a target zone!")
                return
        elif args[0].lower() == 'logics':
            try:
                if len(args[1].split(" ")) != 1:
                    user.writePlain('Proper format is logics modulename. No spaces.\r\n>> ')
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
            except IndexError:
                user.writePlain("You must specify a logic module!")
                return
        elif args[0] == '':
            self.displayPortalEditPage(user)
        
        else:
            user.writePlain('Invalid command! Type help for help! \r\n>> ')
            
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
                if eachTemp.name.lower() == args[1].lower():
                    x = x + 1
                    y = y + 1
                    # Need a local variable to get the value of eachTemp into the new block below
                    #  Updated the if/else clause below to reflect using the new local variable tmp -V
                    tmp = eachTemp
                    if x == 3:
                        user.writePlain('['+str(tmp.id_num)+'] ['+tmp.name+']\r\n')
                        x = 0
                    else:
                        user.writePlain('['+str(tmp.id_num)+'] ['+tmp.name+']\r\n')
            if y != 0:
                user.writePlain('>> ')
                return
            else:
                user.writePlain('Could not find any templates matching that parameter!\r\n>> ')
                return
            
        elif args[0].lower() == 'edit':

            try:
                int(args[1])
            except exceptions.ValueError:
                user.writePlain("<red>Warning: Improper argument passed to edit function!\r\n")
                user.writePlain("<green>Correct Usage: edit <ID Number>\r\n")
                user.writePlain(' '.join(["<white>Please perform a search for the template you'd like to edit.\r\n",\
                                          "This will give you the correct ID number for reference.\r\n",\
                                          "\r\n>>"]))
                return

            
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
                newTemplate.id_num            = int(args[1])
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
                if len(args) < 2:
                    user.writePlain("Proper format is: stats <name> <value>\r\n>>")
                    return
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
            
    def mobInstanceEditProcess(self, user, args):
        args = args.split(" ", 1)
        try:
            if args[0].lower() == 'name':
                file = MudConst.mob_dir+user.curWorkingCharInstance.name+'.xml'
                try:
                     os.remove(file)
                except:
                     pass
                user.curWorkingCharInstance.name = args[1]
                self.displayMobInstanceEditPage(user)
                return
            elif args[0] == '':
                self.displayMobInstanceEditPage(user)
                return
            elif args[0].lower() == 'desc':
                user.curWorkingCharInstance.desc = args[1]
                self.displayMobInstanceEditPage(user)
                return
            
            elif args[0].lower() == 'logics':
                try:
                    if args[1] in user.curWorkingCharInstance.logic_modules:
                        user.curWorkingCharInstance.removeLogic(args[1])
                        self.displayMobInstanceEditPage(user)
                    else:
                        user.curWorkingCharInstance.addLogic(args[1])
                        self.displayMobInstanceEditPage(user)
                except ImportError:
                    user.writePlain("Logic module not found!\r\n>> ")
                    return
                
            elif args[0].lower() == 'stats':
                tmp = args[1].split(" ")
                if len(tmp) != 2:
                    user.writePlain('Proper format is: stats name value!\r\n>> ')
                    return
                else:
                    if user.curWorkingCharInstance.statistics.has_key(tmp[0]):
                        del user.curWorkingCharInstance.statistics[tmp[0]]
                        self.displayMobEditPage(user)
                    else:
                        user.curWorkingCharInstance.statistics[tmp[0]] = tmp[1]
                        self.displayMobInstanceEditPage(user)
            elif args[0].lower() == 'help':
                user.writePlain('This is the Mob Instance Editor. It edits specific instances of mob templates.\r\n')
                user.writePlain('Type what you see in [] to edit them. Such as: name New Name.\r\n')
                user.writePlain('If a stat exists and you want to remove it, just type stats statname.\r\n')
                user.writePlain('To change or add a stat value, type stats statname value.\r\n')
                user.writePlain('>> ')
                return
            else:
                user.writePlain("Invalid choice! Type help for help!\r\n>> ")
                return
            
        except ValueError:
            user.writePlain('Fix me in MobEditProcess!\r\n>> ')
        except IndexError:
            user.writePlain('You must specify a value! Type help for help!\r\n>> ')
            
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
                if eachTemp.name.lower() == args[1].lower():
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
            
    def itemInstanceEditProcess(self, user, args):
        args = args.split(" ", 1)
        try:
            if args[0].lower() == 'name':
                user.curWorkingItemInstance.name = args[1]
                self.displayItemInstanceEditPage(user)
                return
            elif args[0].lower() == 'desc':
                user.curWorkingItemInstance.desc = args[1]
                self.displayItemInstanceEditPage(user)
                return
            elif args[0].lower() == 'logics':
                if args[1] in user.curWorkingItemInstance.logics:
                    user.curWorkingItemInstance.removeLogic(args[1])
                    self.displayItemInstanceEditPage(user)
                else:
                    user.curWorkingItemInstance.addLogic(args[1])
                    self.displayItemInstanceEditPage(user)
            elif args[0].lower() == 'stats':
                tmp = args[1].split(" ")
                if len(tmp) != 2:
                    user.writePlain('Proper format is: stats name value!\r\n>> ')
                    return
                else:
                    if user.curWorkingItemInstance.statistics.has_key(tmp[0]):
                        del user.curWorkingItemInstance.statistics[tmp[1]]
                        self.displayItemInstanceEditPage(user)
                    else:
                        user.curWorkingItemInstance.statistics[tmp[0]] = tmp[1]
                        self.displayItemInstanceEditPage(user)
            elif args[0].lower() == 'help':
                user.writePlain('This is the Item Instance Editor. It edits specific instances of item templates.\r\n')
                user.writePlain('Type what you see in [] to edit them. Such as: name New Name.\r\n')
                user.writePlain('If a stat exists and you want to remove it, just type stats statname.\r\n')
                user.writePlain('To change or add a stat value, type stats statname value.\r\n')
                user.writePlain('>> ')
                return
            else:
                user.writePlain("Not a valid choice! Type help for help! \r\n>> ")
                return
        except ValueError:
            print sys.exc_info()[1]
            user.writePlain('Fix me in ItemInstanceEditProcess!\r\n>> ')
        except IndexError:
            user.writePlain("Proper format is: stats name (value). Type help for help!")
            
    def displayZoneEditPage(self, user):
        pass
        #    user.writePlain('<cls>Zone Creation and Editing Section\r\n\r\n')
        #    user.writePlain('[Name]       :  '+user.curWorkingZone.name+'\r\n')
        #    user.writePlain('[ID]         :  '+str(user.curWorkingZone.id_num)+'\r\n')
        #    y = 0
        #    user.writePlain('[Permissions]\r\n\r\n')
        #    for eachAllowed in user.curWorkingZone.allowed:
        #        if y == 4:
        #            user.writePlain('\r\n')
        #            y = 0
        #        user.writePlain(eachAllowed+'    ')
        #    y = 0
        #    user.writePlain('\r\n\r\n[Logics]\r\n')
        #    for eachModule in user.curWorkingZone.logic_modules.keys():
        #        if y == 4:
        #            user.writePlain('\r\n')
        #            y = 0
        #        user.writePlain(eachModule+'    ')
        #
        #    user.writePlain('\r\n\r\n>> ')
    
    def displayZoneListPage(self, user):
        pass
        #user.writePlain('<cls><bright><white>SlitherMUD OLC Main Menu\r\n\r\n')
        #user.writePlain('<under><bright><white>Zone ID<r>    <under><bright><white>Zone Name<r>\r\n')
        #for eachZone in self.cur_zones.keys():
        #    user.writePlain('\r\n'+str(eachZone)+'         '+self.cur_zones[eachZone].name+'\r\n')
        #user.writePlain('>>')
        
    def displayRoomListPage(self, user):
        pass
        #user.writePlain('<cls><bright><white>SlitherMUD OLC Room List Page<r>\r\n\r\n')
        #user.writePlain('Rooms range from 1 to ')
        #cnt = 1
        #for eachRoom in user.curWorkingZone.rooms.keys():
        #    cnt = cnt + 1
        #user.writePlain(str(cnt)+'.\r\n')
        #user.writePlain('>> ')
        
    def displayRoomEditPage(self, user):
        try:
            desc = self.formatOutput(user.curWorkingRoom.desc)
            user.writePlain('<cls><white><bright>SlitherMUD OLC Room Edit Page<r>\r\n\r\n')
            user.writePlain('<cyan>[Name]     <r>:   <green>'+user.curWorkingRoom.name+'<r>\r\n')
            user.writePlain('<cyan>[ID  ]     <r>:   <green>'+str(user.curWorkingRoom.id_num)+'\r\n')
            user.writePlain('<cyan>[Desc]<r>\r\n'+desc+'\r\n')
            user.writePlain('\r\n<bright><red>Portals<r>\r\n')
            x = 0
            for eachPortal in user.curWorkingRoom.portals.keys():
                if x == 4:
                    user.writePlain('\r\n'+str(eachPortal)+'] '+user.curWorkingRoom.portals[eachPortal].name+'    ')
                    x = 0
                else:
                    user.writePlain('['+str(eachPortal)+'] '+ user.curWorkingRoom.portals[eachPortal].name+'   ')
                    x = x + 1
            x = 0
            user.writePlain('\r\n\r\n<bright><red>[Logics]<r>\r\n')
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
        user.writePlain('<cyan>[Name   ]   <r>: <green>'+user.curWorkingPortal.name+'\r\n')
        user.writePlain('<cyan>[ID     ]   <r>: <green>'+str(user.curWorkingPortal.id_num)+'\r\n')
        user.writePlain('<cyan>[TargetR]   <r>: <green>'+str(user.curWorkingPortal.target_room)+'\r\n')
        user.writePlain('<cyan>[TargetZ]   <r>: <green>'+str(user.curWorkingPortal.target_zone)+'\r\n')
        user.writePlain('\r\n<red><bright>[Logics]<r>\r\n')
        x = 0
        for eachLogic in user.curWorkingPortal.logic_modules.keys():
            if x == 4:
                user.writePlain('\r\n')
                user.writePlain(eachLogic+'  ')
                x = 0
            else:
                user.writePlain(eachLogic+'  ')
                x = x + 1
        user.writePlain('\r\n\r\n>> ')
                
    def displayMobEditPage(self, user):
        user.writePlain('<cls><white>SlitherMUD OLC MOB Template Edit Page\r\n\r\n')
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
            
    def displayMobInstanceEditPage(self, user):
        user.writePlain('<cls><white>SlitherMUD OLC MOB Editor\r\n\r\n')
        user.writePlain('[Name] '+user.curWorkingCharInstance.name+'\r\n')
        user.writePlain('[ID  ] '+str(user.curWorkingCharInstance.id_num)+'\r\n')
        user.writePlain('Template: '+str(user.curWorkingCharInstance.template_id)+'\r\n')
        user.writePlain('[Desc] '+user.curWorkingCharInstance.desc+'\r\n')
        x = 0
        user.writePlain('\r\n\r\n[Logics]\r\n')
        for eachLogic in user.curWorkingCharInstance.logic_modules:
            if x == 3:
                user.writePlain(eachLogic+'\r\n')
                x = 0
            else:
                user.writePlain(eachLogic+ '  ')
                x = x + 1
        x = 0
        user.writePlain('\r\n\r\n[Stats]\r\n')
        for eachStat in user.curWorkingCharInstance.statistics.keys():
            if x == 3:
                user.writePlain('('+eachStat+') ('+str(user.curWorkingCharInstance.statistics[eachStat])+')\r\n')
                x = 0
            else:
                user.writePlain('('+eachStat+') ('+str(user.curWorkingCharInstance.statistics[eachStat])+')  ')
                x = x + 1
        user.writePlain('\r\n\r\n>> ')
        
    def displayMobSelectPage(self, user):
        try:
            user.writePlain('<cls><bright><white>---------------------<green>MOB TEMPLATE EDITOR<bright><white>----------------------\r\n')
            user.writePlain('<white>  To search for a mob template by name, type: <cyan>search <name><white>.\r\n')
            user.writePlain('  To edit that template, type: <cyan>edit <idnum><white>.\r\n')
            user.writePlain('  To create a new template, type: <cyan>new<white>.\r\n')
            user.writePlain('  To save, type: <cyan>save<white>.\r\n')
            user.writePlain('<bright><white>---------------------------<green>SLITHER<bright><white>----------------------------\r\n>><r>')
        except TypeError:
            pass
        
    def displayItemInstanceEditPage(self, user):
        user.writePlain('<cls><white>SlitherMUD OLC Template Edit Page\r\n\r\n')
        user.writePlain('[Name] '+user.curWorkingItemInstance.name+'\r\n')
        user.writePlain('[ID  ] '+str(user.curWorkingItemInstance.id_num)+'\r\n')
        user.writePlain('Template: '+str(user.curWorkingItemInstance.template_id)+'\r\n')
        user.writePlain('[Desc] '+user.curWorkingItemInstance.desc+'\r\n')
        x = 0
        user.writePlain('\r\n\r\n[Logics]\r\n')
        for eachLogic in user.curWorkingItemInstance.logic_modules.keys():
            if x == 3:
                user.writePlain(eachLogic+'\r\n')
                x = 0
            else:
                user.writePlain(eachLogic+ '  ')
                x = x + 1
        x = 0
        user.writePlain('\r\n\r\n[Stats]\r\n')
        for eachStat in user.curWorkingItemInstance.statistics.keys():
            if x == 3:
                user.writePlain('('+eachStat+') ('+user.curWorkingItemInstance.statistics[eachStat]+')\r\n')
                x = 0
            else:
                user.writePlain('('+eachStat+') ('+user.curWorkingItemInstance.statistics[eachStat]+')  ')
                x = x + 1
        user.writePlain('\r\n\r\n>> ')
        
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
            user.writePlain('<cls><bright><white>---------------------<green>ITEM TEMPLATE EDITOR<bright><white>---------------------\r\n')
            user.writePlain('<white>  To search for a item template by name, type: <cyan>search <name><white>.\r\n')
            user.writePlain('  To edit that template, type: <cyan>edit <idnum><white>.\r\n')
            user.writePlain('  To create a new template, type: <cyan>new<white>.\r\n')
            user.writePlain('<bright><white>---------------------------<green>SLITHER<bright><white>----------------------------\r\n>><r>')
        except TypeError:
            pass
        
    def createNewZone(self, user):
        pass
        #tmp = MudZone.MudZone()
        #tmp.name = ''
        #tmp.allowed.append(user.name)
        #x = 0
        #for eachKey in self.cur_zones.keys():
        #    x = x + eachKey
        #tmp.id_num = x
        #return tmp
    
    def formatOutput(self, data):
        res = ''
        res = textwrap.fill(data, 80)
        res = res.replace('\n', '\r\n')
        #res = res.replace(']', ']\r\n')
        res = res.lstrip()
        return res