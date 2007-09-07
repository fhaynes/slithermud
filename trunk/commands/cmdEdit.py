import os

import MudCommand
import MudAction
import MudActionHandler
import MudDatabase
import MudWorld
import MudConst

class cmdEdit(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.cmdName    = "edit"
        self.helpText   = '''This lets you edit the name or desc of things outside of the OLC.'''
        self.helpText  += '''\r\nYou can edit: item room zone mob or portal.'''
        self.helpText  += '''\r\nMobs, portals, and items require an ID, and must be in the same room as you.'''
        self.helpText  += '''\r\nTo edit the current room you are in, type edit room.'''
        self.useExample = '''edit room or edit mob 20 or edit item 20'''


    def Process(self, player, args):
        args = args.split(" ", 1)
        if args[0].lower() == 'item':
            try:
                for eachChar in player.roomRef.items.values():
                    if eachChar.id_num == int(args[1]):
                        player.curWorkingZone         = player.zoneRef
                        player.curWorkingRoom         = player.roomRef
                        player.curWorkingItemInstance = eachChar
                        player.login_state            = MudConst.inOlc
                        player.olcState               = MudWorld.world.olcHandler.itemInstanceEditPage
                        MudWorld.world.olcHandler.users.append(player)
                        MudWorld.world.olcHandler.displayItemInstanceEditPage(player)
                        return
                player.writeWithPrompt("Specified ITEM not found in room!")
                return
            except IndexError:
                player.writeWithPrompt("You must specify the ID of a ITEM in the room!")
                return
            
            
            #i_args = args[1].split(" ", 2)
            #if len(i_args) != 3:
            #    player.writeWithPrompt("Proper format is: edit item id field value!")
            #    return
            #tmp = MudDatabase.db.findItem(i_args[0])
            #if tmp == []:
            #    player.writeWithPrompt("Could not find that item ID to edit!")
            #    return
            #if i_args[1].lower() == 'name':
            #    tmp.name = args[2]
            #    player.writeWithPrompt("Done!")
            #    return
            #if i_args[1].lower() == 'desc':
            #    tmp.desc = args[2]
            #    player.writeWithPrompt("Done!")
            #    return
            #if i_args[1].lower() == 'logic':
            #    if tmp.logic_modules.has_key(i_args[2]):
            #        tmp.removeLogic(i_args[2])
            #    else:
            #        try:
            #            tmp.addLogic(i_args[2])
            #        except IndexError:
            #            player.writeWithPrompt("Could not find that logic module!")
            #else:
            #    player.writeWithPrompt("You can only edit name or desc! Use set for other things!")
            #    return
        
        elif args[0].lower() == 'room':
            for x in player.zoneRef.allowed:
                if x.lower() == player.name.lower():
                    player.curWorkingZone = player.zoneRef
                    player.curWorkingRoom = player.roomRef
                    player.login_state    = MudConst.inOlc
                    player.olcState       = MudWorld.world.olcHandler.roomEditPage
                    MudWorld.world.olcHandler.users.append(player)
                    MudWorld.world.olcHandler.displayRoomEditPage(player)
                    return
                    
            player.writeWithPrompt("You do not have permission to edit rooms in this zone!")
            return

            
            
            #r_args = args[1].split(" ", 1)
            #if len(r_args) != 2:
            #    player.writeWithPrompt("Proper format is: edit room field value!")
            #    return
            #for x, y in enumerate(player.zoneRef.allowed):
            #    if y == player.name or player.admin_level == 5:
            #        if r_args[0].lower() == 'name':
            #            player.roomRef.name = r_args[1]
            #            MudWorld.world.handleInput(player, 'look')
            #            return
            #        if r_args[0].lower() == 'desc':
            #            if r_args[1] == 'clear':
            #                player.roomRef.desc = ''
            #                return
            #            else:
            #                player.roomRef.desc += ' '+r_args[1]
            #                MudWorld.world.handleInput(player, 'look')
            #                return
            #        if i_args[0].lower() == 'logic':
            #            if tmp.logic_modules.has_key(i_args[2]):
            #                tmp.removeLogic(i_args[2])
            #            else:
            #                try:
            #                    tmp.addLogic(i_args[2])
            #                except IndexError:
            #                    player.writeWithPrompt("Could not find that logic module!")
            #        else:
            #            player.writeWithPrompt("That is not a valid thing to edit for rooms!")
            #            return
            #player.writeWithPrompt("You do not have permission to edit things in this zone!")
            #return
        
        elif args[0].lower() == 'zone':
            r_args = args[1].split(" ", 1)
            if len(r_args) != 2:
                player.writeWithPrompt("Proper format is: edit zone field value!")
                return
            for x, y in enumerate(player.zoneRef.allowed):
                if y == player.name or player.admin_level == MudConst.implementor:
                    if r_args[0].lower() == 'name':
                        if r_args[1].isdigit():
                            player.writeWithPrompt("Only letters in room names!")
                            return
                        else:
                            player.zoneRef.name = r_args[1]
                            MudWorld.world.handleInput(player, 'look')
                            return
                    if r_args[0].lower() == 'desc':
                        if r_args[1].isdigit():
                            player.writeWithPrompt("Only letters in room descriptions!")
                            return
                        else:
                            player.zoneRef.desc = r_args[1]
                            MudWorld.World.handleInput(player, 'look')
                            return
                    if r_args[0].lower() == 'allowed':
                        
                        for x in player.zoneRef.allowed:
                            if x.lower() == r_args[1].lower():
                                player.zoneRef.allowed.remove(r_args[1])
                                player.writeWithPrompt(r_args[1]+' has been disallowed from editing this zone!')
                                return

                        player.zoneRef.allowed.append(r_args[1])
                        player.writeWithPrompt(r_args[1]+' has been granted permission to edit this zone!')
                        print player.zoneRef.allowed
                        return
                    else:
                        player.writeWithPrompt("That is not a valid thing to edit for rooms!")
                        return
            player.writeWithPrompt("You do not have permission to edit things in this zone!")
            return

            
        elif args[0].lower() == 'mob':
            try:
                for eachChar in player.roomRef.characters.values():
                    print eachChar.name
                    if eachChar.id_num == int(args[1]):
                        if eachChar.sockRef != '':
                            player.writeWithPrompt("You cannot edit players! Use Set!")
                            return
                        player.curWorkingZone         = player.zoneRef
                        player.curWorkingRoom         = player.roomRef
                        player.curWorkingCharInstance = eachChar
                        player.login_state            = MudConst.inOlc
                        player.olcState               = MudWorld.world.olcHandler.mobInstanceEditPage
                        MudWorld.world.olcHandler.users.append(player)
                        MudWorld.world.olcHandler.displayMobInstanceEditPage(player)
                        return
                player.writeWithPrompt("Specified MOB not found in room!")
                return
            except IndexError:
                player.writeWithPrompt("You must specify the name of a MOB in the room!")
                return
            
            
                        
            #i_args = args[1].split(" ", 2)
            #if len(i_args) != 3:
            #    player.writeWithPrompt("Proper format is: edit char id field value!")
            #    return
            #tmp = MudDatabase.db.findChar(i_args[0])
            #if tmp == []:
            #    player.writeWithPrompt("Could not find that item ID to edit!")
            #    return
            #if i_args[1].lower() == 'name':
            #    file = MudConst.mob_dir+tmp.name+'.xml'
            #    os.remove(file)
            #    tmp.name = i_args[2]
            #    player.writeWithPrompt("Done!")
            #    return
            #if i_args[1].lower() == 'desc':
            #    tmp.desc = i_args[2]
            #    player.writeWithPrompt("Done!")
            #    return
            #if i_args[1].lower() == 'logic':
            #    if tmp.logic_modules.has_key(i_args[2]):
            #        tmp.removeLogic(i_args[2])
            #        player.writeWithPrompt("Logic module removed!")
            #        return
            #    else:
            #        try:
            #            tmp.addLogic(i_args[2])
            #            player.writeWithPrompt("Logic module added!")
            #            return
            #        except IndexError:
            #            player.writeWithPrompt("Could not find that logic module!")
            #else:
            #    player.writeWithPrompt("You can only edit name or desc! Use set for other things!")
            #    return
        
        elif args[0].lower() == 'portal':
            for x in player.zoneRef.allowed:
                if x.lower() == player.name.lower():
                    
                    try:
                        for eachPortal in player.roomRef.portals.values():
                            if int(args[1]) == eachPortal.id_num:
                                player.curWorkingZone   = player.zoneRef
                                player.curWorkingRoom   = player.roomRef
                                player.curWorkingPortal = eachPortal
                                player.login_state      = MudConst.inOlc
                                player.olcState         = MudWorld.world.olcHandler.portalEditPage
                                MudWorld.world.olcHandler.users.append(player)
                                MudWorld.world.olcHandler.displayPortalEditPage(player)
                                return
                        player.writeWithPrompt("Invalid portal name!")
                        return
                    except IndexError:
                        player.writeWithPrompt("You must specify a portal name!")
                        return
            player.writeWithPrompt("You do not have permission to edit portals in this zone!")
                
            #if len(i_args) != 3:
            #    player.writeWithPrompt("Improper format! Use: edit portal id name/desc/targetroom/targetzone value!")
            #    return
            #if player.roomRef.portals.has_key(int(i_args[0])):
            #    tmp = player.roomRef.portals[int(i_args[0])]
            #else:
            #    player.writeWithPrompt("Invalid Portal ID!")
            #    return
            #
            #if i_args[1].lower() == 'name':
            #    tmp.name = args[2]
            #    player.writeWithPrompt("Done!")
            #    return
            #elif i_args[1].lower() == 'desc':
            #    tmp.desc = args[2]
            #    player.writeWithPrompt("Done!")
            #    return
            #elif i_args[1].lower() == 'troom':
            #    if not i_args[2].isdigit():
            #        player.writeWithPrompt("Target rooms can only be numbers!")
            #        return
            #    tmp.target_room = int(args[2])
            #    player.writeWithPrompt("Done!")
            #    return
            #elif i_args[1].lower() == 'tzone':
            #    if not i_args[2].isdigit():
            #        player.writeWithPrompt("Target zones can only be numbers!")
            #        return
            #    tmp.target_zone = int(args[2])
                #player.writeWithPrompt("Done!")
                #return
            #else:
            #    player.writeWithPrompt("You can only edit: name/desc/troom/tzone! Troom/tzone are destination room and zone!")
            #    return
            
        else:
            player.writeWithPrompt("Not a valid choice!")
            return


edit = cmdEdit()