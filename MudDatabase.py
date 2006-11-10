"""
Database related classes.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import os
import copy
import cPickle as pickle
from xml.sax import ContentHandler
from xml.sax import make_parser
import string

import MudConst
import MudItem
import MudCharacter
import MudZone
import MudRoom
import MudPortal
import MudItem

import cmdLook
import cmdSay
import cmdOlc
import cmdGo
import cmdWho
import cmdIcreate
import cmdMcreate
import cmdSet
import cmdSearch
import cmdHelp
import cmdCopyover
import cmdGet
import cmdQuit
import cmdInventory
import cmdDrop
import cmdAssign
import cmdObliterate
import cmdInfo
import cmdGrant
import cmdEdit
import cmdNewzone
import cmdWarp
import cmdZonelist
import cmdRemovezone
import cmdBuildwalk
import cmdVari
import cmdSavezone
import cmdGive
import cmdNewportal
import cmdDelzone
import cmdPromote

def nw(text):
    "Remove redundant whitespace from a string"
    return ' '.join(text.split())

class CharTemplateHandler(ContentHandler):
    def __init__(self):
        self.inLogic = 0
        self.inStat  = 0
        self.inCom   = 0
    def startElement(self, name, attrs):
        if name == 'c_template':
            self.newTemp = MudCharacter.MudCharacterTemplate()
            self.newTemp.name = str(nw(attrs.get('name', "")))
            self.newTemp.id_num = int(nw(attrs.get('id_num', "")))
            self.newTemp.desc = str(nw(attrs.get('desc', "")))
        elif name == 'logic':
            self.inLogic = 1
        elif name == 'command':
            self.inCom = 1
        elif name == 'stat':
            self.inStat = 1
        else:
            pass
        
    def endElement(self, name):
        if name == 'logic':
            self.inLogic = 0
        elif name == 'command':
            self.inCom = 0
        elif name == 'stat':
            self.inStat = 0
        else:
            pass
        
    def characters(self, ch):
        ch = str(ch)
        if self.inCom:
            self.newTemp.commands.append(ch)
        elif self.inLogic:
            self.newTemp.logics.append(ch)
        elif self.inStat:
            x, y = ch.split(":", 1)
            if y.isdigit():
                self.newTemp.statistics[x] = int(y)
            else:
                self.newTemp.statistics[x] = y
                
    def endDocument(self):
        db.c_templates[self.newTemp.id_num] = self.newTemp
        
class ItemTemplateHandler(ContentHandler):
    def __init__(self):
        self.inLogic = 0
        self.inStat  = 0
        self.inCom   = 0
    def startElement(self, name, attrs):
        if name == 'i_template':
            self.newTemp = MudCharacter.MudCharacterTemplate()
            self.newTemp.name = str(nw(attrs.get('name', "")))
            self.newTemp.id_num = int(nw(attrs.get('id_num', "")))
            self.newTemp.desc = str(nw(attrs.get('desc', "")))
        elif name == 'logic':
            self.inLogic = 1
        elif name == 'command':
            self.inCom = 1
        elif name == 'stat':
            self.inStat = 1
        else:
            pass
        
    def endElement(self, name):
        if name == 'logic':
            self.inLogic = 0
        elif name == 'command':
            self.inCom = 0
        elif name == 'stat':
            self.inStat = 0
        else:
            pass
        
    def characters(self, ch):
        ch = str(ch)
        if self.inCom:
            self.newTemp.commands.append(ch)
        elif self.inLogic:
            self.newTemp.logics.append(ch)
        elif self.inStat:
            x, y = ch.split(":", 1)
            if y.isdigit():
                self.newTemp.statistics[x] = int(y)
            else:
                self.newTemp.statistics[x] = y
                
    def endDocument(self):
        db.i_templates[self.newTemp.id_num] = self.newTemp

    
class CharHandler(ContentHandler):
    def __init__(self):
        self.inCharacter = 0
        self.inCommand   = 0
        self.inItem      = 0
        self.inCStat     = 0
        self.inCLogic    = 0
        self.inIStat     = 0
        self.inILogic    = 0
    
    def startElement(self, name, attrs):
        if name == 'character':
            self.inCharacter = 1
            self.newChar = MudCharacter.MudCharacter()
            self.newChar.name = str(nw(attrs.get('name', "")))
            self.newChar.id_num = int(nw(attrs.get('id_num', "")))
            self.newChar.template_id = int(nw(attrs.get('template_id', "")))
            self.newChar.zone   = int(nw(attrs.get('zone', "")))
            self.newChar.room   = int(nw(attrs.get('room', "")))
            self.newChar.admin_level = int(nw(attrs.get('a_l', "")))
            self.newChar.password = str(nw(attrs.get('password', "")))
            self.newChar.desc = str(nw(attrs.get('desc', "")))
            
        elif name == 'command':
            self.inCommand = 1
        elif name == 'cstat':
            self.inCStat = 1
        elif name == 'clogic':
            self.inCLogic = 1
        elif name == 'ilogic':
            self.inILogic = 1
        elif name == 'istat':
            self.inIStat = 1
        elif name == 'item':
            self.inItem = 1
            self.newItem = MudItem.MudItem()
            self.newItem.name = str(nw(attrs.get('name', "")))
            self.newItem.id_num = int(nw(attrs.get('id_num', "")))
            self.newItem.desc   = str(nw(attrs.get('desc', "")))
            self.newItem.template_id = int(nw(attrs.get('t_id', "")))
            self.newItem.quantity = int(nw(attrs.get('quan', "")))
            self.newItem.isQuantity = str(nw(attrs.get('isquan', "")))
            self.newItem.zone = None
            self.newItem.room = None
            self.newItem.owner = self.newChar.name

        else:
            pass
    
    def endElement(self, name):
        if name == 'character':
            self.inCharacter = 0
        elif name == 'command':
            self.inCommand = 0
        elif name == 'cstat':
            self.inCStat = 0
        elif name == 'clogic':
            self.inCLogic = 0
        elif name == 'ilogic':
            self.inILogic = 0
        elif name == 'istat':
            self.inIStat = 0
        elif name == 'item':
            self.inItem = 0
            self.newChar.addItem(self.newItem)
            db.addItem(self.newItem)
        else:
            pass
        
    def characters(self, ch):
        ch = str(ch)
        if self.inCommand:
            self.newChar.addCommand(ch, db.commands[ch])
        elif self.inCLogic:
            self.newChar.addLogic(ch)
        elif self.inCStat:
            x = ch.split(":", 1)
            y = x[0]
            z = x[1]
            if z.isdigit():
                self.newChar.addStat(y, int(z))
            else:
                self.newChar.addStat(y, z)
        elif self.inILogic:
            self.newItem.addLogic(ch)
        elif self.inIStat:
            x = ch.split(":", 1)
            y = x[0]
            z = x[1]
            self.newItem.statistics[x] = y
        else:
            pass
        
    def endDocument(self):
        try:
            self.newChar.setZone(self.newChar.zone)
        except:
            self.newChar.setZone(1)
        try:
            self.newChar.setRoom(self.newChar.room)
        except:
            self.newChar.setRoom(1)
        db.c_tmp = self.newChar
        
class ZoneHandler(ContentHandler):
    def __init__(self):

        # Initialize the flag to false
        self.inZinfo   = 0
        self.inRoom    = 0
        self.inPortal  = 0
        self.inRLogic  = 0
        self.inPLogic  = 0
        self.inAllowed = 0
        self.inItem    = 0
        self.inILogic  = 0
        self.inIStat   = 0

    def startElement(self, name, attrs):
        # If it's a comic element, save the title and issue
        if name == 'zinfo':
            self.inZinfo = 1
            self.newZone        = MudZone.MudZone()
            self.newZone.name   = str(nw(attrs.get('name', "")))
            self.newZone.id_num = int(nw(attrs.get('id_num', "")))
        elif name == 'allowed':
            self.inAllowed = 1
        elif name == 'room':
            self.inRoom = 1
            self.newRoom      = MudRoom.MudRoom()
            self.newRoom.name = str(nw(attrs.get('name', "")))
            self.newRoom.id_num   = int(nw(attrs.get('id_num', "")))
            self.newRoom.desc = str(nw(attrs.get('desc', "")))
            self.newZone.addRoom(self.newRoom)
        elif name == 'portal':
            self.inPortal = 1
            self.newPortal = MudPortal.MudPortal()
            self.newPortal.name = str(nw(attrs.get('name', "")))
            self.newPortal.id_num = int(nw(attrs.get('id_num', "")))
            self.newPortal.desc = str(nw(attrs.get('desc', "")))
            self.newPortal.target_zone = int(nw(attrs.get('tz', "")))
            self.newPortal.target_room = int(nw(attrs.get('tr', "")))
            self.newRoom.addPortal(self.newPortal)
        elif name == 'item':
            self.inItem = 1
            self.newItem = MudItem.MudItem()
            self.newItem.name = str(nw(attrs.get('name', "")))
            self.newItem.id_num = int(nw(attrs.get('id_num', "")))
            self.newItem.desc   = str(nw(attrs.get('desc', "")))
            self.newItem.template_id = int(nw(attrs.get('t_id', "")))
            self.newItem.quantity = int(nw(attrs.get('quan', "")))
            self.newItem.isQuantity = str(nw(attrs.get('isquan', "")))
            self.newItem.zone = self.newZone
            self.newItem.room = self.newRoom
            self.newRoom.addItem(self.newItem)
            db.addItem(self.newItem)
        elif name == 'ilogic':
            self.inILogic = 1
        elif name == 'istat':
            self.inIStat = 1
        elif name == 'rlogic':
            self.inRLogic = 1
        elif name == 'plogic':
            self.inPLogic = 1
        else:
            pass

    def endElement(self, name):
        if name == 'zinfo':
            self.inZinfo = 0    
        elif name == 'allowed':
            self.inAllowed = 0
        elif name == 'room':
            self.inRoom = 0
        elif name == 'portal':
            self.inPortal = 0
        elif name == 'rlogic':
            self.inRLogic = 0
        elif name == 'plogic':
            self.inPLogic = 0
        elif name == 'item':
            self.inItem = 0
        elif name == 'ilogic':
            self.inILogic = 0
        elif name == 'istat':
            self.inIStat = 0
        else:
            pass
        
    def characters(self, ch):
        ch = str(ch)
        if self.inAllowed:
            self.newZone.allowed.append(ch)
        elif self.inRLogic:
            self.newRoom.addLogic(ch)
        elif self.inPLogic:
            self.newPortal.addLogic(ch)
        elif self.inILogic:
            self.newItem.addLogic(ch)
        elif self.inIStat:
            x = ch.split(":", 1)
            y = x[0]
            z = x[1]
            self.newItem.statistics[x] = y
            
            
    def endDocument(self):
        db.tmp = self.newZone
            
class DatabaseManager:
    """
    This class handles saving/loading world data and players from the db.
    """
    
    def __init__(self):
        self.characters   = {}
        self.c_templates  = {}
        self.items        = {}
        self.i_templates  = {}
        self.zones        = {}

        
        self.next_item_id = 0
        self.next_char_id = 0
        self.next_zone_id = 0
        
        self.commands     = {}
        self.commands['promote'] = cmdPromote.promote
        self.commands['look'] = cmdLook.look
        self.commands['say']  = cmdSay.say
        self.commands['go']   = cmdGo.go
        self.commands['who']  = cmdWho.who
        self.commands['get']  = cmdGet.get
        self.commands['quit'] = cmdQuit.quit
        self.commands['help'] = cmdHelp.help
        self.commands['drop'] = cmdDrop.drop
        self.commands['give'] = cmdGive.give
        self.commands['inventory'] = cmdInventory.inventory
        self.commands['olc']  = cmdOlc.olc
        self.commands['icreate'] = cmdIcreate.icreate
        self.commands['mcreate'] = cmdMcreate.mcreate
        self.commands['set']  = cmdSet.set
        self.commands['search'] = cmdSearch.search
        self.commands['copyover'] = cmdCopyover.copyover
        self.commands['obliterate'] = cmdObliterate.obliterate
        self.commands['assign'] = cmdAssign.assign
        self.commands['info']   = cmdInfo.info
        self.commands['grant']  = cmdGrant.grant
        self.commands['edit']   = cmdEdit.edit
        self.commands['newzone'] = cmdNewzone.newzone
        self.commands['warp'] = cmdWarp.warp
        self.commands['zonelist'] = cmdZonelist.zonelist
        self.commands['removezone'] = cmdRemovezone.removezone
        self.commands['buildwalk'] = cmdBuildwalk.buildwalk
        self.commands['vari'] = cmdVari.vari
        self.commands['savezone'] = cmdSavezone.savezone
        self.commands['newportal'] = cmdNewportal.newportal
        self.commands['delzone'] = cmdDelzone.delzone
    
    # Command loading functions
    def loadStdCmds(self, user):
        user.addCommand("say",  cmdSay.say)
        user.addCommand("look", cmdLook.look)
        user.addCommand("go",   cmdGo.go)
        user.addCommand("olc",  cmdOlc.olc)
        user.addCommand("who",  cmdWho.who)
        user.addCommand("help", cmdHelp.help)
        user.addCommand("get", cmdGet.get)
        user.addCommand("quit", cmdQuit.quit)
        user.addCommand("inventory", cmdInventory.inventory)
        user.addCommand("drop", cmdDrop.drop)
        user.addCommand("give", cmdGive.give)
    
    def loadBuilderCmds(self, user):
        user.addCommand("icreate", cmdIcreate.icreate)
        user.addCommand("mcreate", cmdMcreate.mcreate)
        user.addCommand("set",     cmdSet.set)
        user.addCommand("search",  cmdSearch.search)
        user.addCommand("obliterate", cmdObliterate.obliterate)
        user.addCommand("info", cmdInfo.info)
        user.addCommand("edit", cmdEdit.edit)
        user.addCommand("warp", cmdWarp.warp)
        user.addCommand("zonelist", cmdZonelist.zonelist)
        user.addCommand("savezone", cmdSavezone.savezone)
        user.addCommand("newportal", cmdNewportal.newportal)
        user.addCommand("buildwalk", cmdBuildwalk.buildwalk)
        
    def loadAllCmds(self, user):
        user.addCommand("icreate", cmdIcreate.icreate)
        user.addCommand("mcreate", cmdMcreate.mcreate)
        user.addCommand("set",     cmdSet.set)
        user.addCommand("search",  cmdSearch.search)
        user.addCommand("copyover", cmdCopyover.copyover)
        user.addCommand("assign", cmdAssign.assign)
        user.addCommand("obliterate", cmdObliterate.obliterate)
        user.addCommand("info", cmdInfo.info)
        user.addCommand("grant", cmdGrant.grant)
        user.addCommand("edit", cmdEdit.edit)
        user.addCommand("newzone", cmdNewzone.newzone)
        user.addCommand("warp", cmdWarp.warp)
        user.addCommand("zonelist", cmdZonelist.zonelist)
        user.addCommand("removezone", cmdRemovezone.removezone)
        user.addCommand("buildwalk", cmdBuildwalk.buildwalk)
        user.addCommand("vari", cmdVari.vari)
        user.addCommand("savezone", cmdSavezone.savezone)
        user.addCommand("newportal", cmdNewportal.newportal)
        user.addCommand("delzone", cmdDelzone.delzone)
    # Saving and loading functions
    def saveIds(self):
        tmp = open(MudConst.id_data_file, 'w')
        tmp.write('ITEM '+str(self.next_item_id)+'\r\n')
        tmp.write('CHAR '+str(self.next_char_id)+'\r\n')
        tmp.write('ZONE '+str(self.next_zone_id)+'\r\n')
        tmp.close()
        
    def loadIds(self):
        tmp = open(MudConst.id_data_file, 'r')
        lines = tmp.readlines()
        i_tmp = lines[0][5:].strip('\r\n')
        c_tmp = lines[1][5:].strip('\r\n')
        z_tmp = lines[2][5:].strip('\r\n')
        self.next_item_id = int(i_tmp)
        self.next_char_id = int(c_tmp)
        self.next_zone_id = int(z_tmp)
        tmp.close()
        
    def saveZoneToDisk(self, zone):
        zone_dir = MudConst.zone_dir+os.sep+zone.name.replace(" ", "")
        if os.path.exists(zone_dir) and os.path.isdir(zone_dir):
            pass
        else:
            os.mkdir(zone_dir)
            
        file = open(zone_dir+os.sep+zone.name.replace(" ", "")+'.xml', 'w')
        file.write('<mud_zone>\r\n')
        file.write('  <zinfo name="'+zone.name+'" id_num="'+str(zone.id_num)+'">\r\n')
        for x in zone.allowed:
            file.write('    <allowed>'+x+'</allowed>\r\n')
        file.write('  </zinfo>\r\n')
        for eachRoom in zone.rooms.values():
            file.write('  <room name="'+eachRoom.name+'" id_num="'+str(eachRoom.id_num)+'" desc="'+eachRoom.desc+'">\r\n')
            for x in eachRoom.logic_modules.keys():
                file.write('    <rlogic>'+x+'</rlogic>\r\n')
            for x in eachRoom.portals.values():
                file.write('    <portal name="'+x.name+'" id_num="'+str(x.id_num)\
+'" tz="'+str(x.target_zone)+'" tr="'+str(x.target_room)+'" desc="'+x.desc+'">\r\n')
                for y in x.logic_modules.keys():
                    file.write('      <plogic>'+y+'</plogic>\r\n')
                file.write('    </portal>\r\n')
            for x in eachRoom.items.values():
                file.write('      <item name="'+x.name+'" id_num="'+str(x.id_num)\
+'" quan="'+str(x.quantity)+'" isquan="'+str(x.isQuantity)+'" t_id="'+str(x.template_id)+'" desc="'+x.desc+'">\r\n')
                for eachStat in x.statistics.keys():
                    file.write('        <istat>'+eachStat+':'+eachStat.statistics[x]+'</istat>\r\n')
                for eachLogic in x.logic_modules.keys():
                    file.write('        <ilogic>'+eachLogic+'</ilogic>\r\n')
                file.write('      </item>\r\n')
            file.write('  </room>\r\n')
        file.write('</mud_zone>\r\n')
        file.close()

        return
        
    def loadZoneFromDisk(self, zone):
        zone_dir = MudConst.zone_dir + zone
        if os.path.exists(zone_dir) and os.path.isdir(zone_dir):
            p = make_parser()
            zh = ZoneHandler()
            p.setContentHandler(zh)
            p.parse(zone_dir+os.sep+zone+'.xml')
            return self.tmp
        else:
            print "Fix me in LoadZoneFromDisk"
            
    def deleteZoneFromDisk(self, zone):
        zone_dir = MudConst.zone_dir+zone.replace(" ", "")+os.sep+zone.replace(" ", "")+'.xml'
        os.remove(zone_dir)
        os.rmdir(MudConst.zone_dir+zone.replace(" ", "")+os.sep)
            
        tmp = open(MudConst.load_list, 'r')
        lines = tmp.readlines()
        tmp.close()
        lines.remove(zone.replace(" ", ""))
        tmp = open(MudConst.load_list, 'w')
        for eachLine in lines:
            tmp.write(eachLine)
        tmp.close()
    
    def saveCharToDisk(self, p_object):
        """
        This pickles the player object to disk.
        
        Accepts the player object to be pickled as an argument.
        """
        if p_object.sockRef != '':
            char_file = MudConst.player_dir+os.sep+str(p_object.name)+'.xml'
        else:
            char_file = MudConst.mob_dir+os.sep+str(p_object.name)+'.xml'
        tmp = file(char_file, 'w')
        tmp.write('<character name="'+p_object.name+'" id_num="'+str(p_object.id_num)+\
'" zone="'+str(p_object.zone)+'" room="'+str(p_object.room)+'" a_l="'+str(p_object.admin_level)\
+'" password="'+p_object.password+'" desc="'+p_object.desc+'" template_id="'+str(p_object.template_id)+'">\r\n')
        for eachCommand in p_object.commands.keys():
            tmp.write('  <command>'+eachCommand+'</command>\r\n')
        for eachLogic in p_object.logic_modules.keys():
            tmp.write('  <clogic>'+eachLogic+'</clogic>\r\n')
        for x in p_object.items.values():
                    tmp.write('  <item name="'+x.name+'" id_num="'+str(x.id_num)\
+'" quan="'+str(x.quantity)+'" isquan="'+str(x.isQuantity)+'" t_id="'+str(x.template_id)+'" desc="'+x.desc+'">\r\n')
                    for eachStat in x.statistics.keys():
                        tmp.write('    <istat>'+eachStat+':'+eachStat.statistics[x]+'</istat>\r\n')
                    for eachLogic in x.logic_modules.keys():
                        tmp.write('    <ilogic>'+eachLogic+'</ilogic>\r\n')
                    tmp.write('  </item>\r\n')
        for eachStat in p_object.statistics.keys():
            tmp.write('  <cstat>'+eachStat+':'+str(p_object.statistics[eachStat])+'</cstat>\r\n')
        tmp.write('</character>')
            
        tmp.close()
    
    def loadMobFromDisk(self, name):
        char_file = MudConst.mob_dir+os.sep+name
        p = make_parser()
        ch = CharHandler()
        p.setContentHandler(ch)
        p.parse(file(char_file, 'r'))
        return self.c_tmp
    
    def loadCharFromDisk(self, name):
        """
        This attempts to load a character from the disk.
        """
        
        char_file = MudConst.player_dir+os.sep+name.capitalize()+'.xml'
        if os.path.isfile(char_file):
            p = make_parser()
            ch = CharHandler()
            p.setContentHandler(ch)
            p.parse(file(char_file, 'r'))
            return self.c_tmp
        else:
            return
        

        
        
    def saveCharTemplateToDisk(self, template):
        """
        This saves a template to disk.
        """
        
        template_file = MudConst.char_template_dir+os.sep+template.name.capitalize()+'.xml'
        tmp = file(template_file, 'w')
        tmp.write('<c_template name="'+template.name+'" id_num="'+str(template.id_num)+\
'" desc="'+template.desc+'">\r\n')
        for eachLogic in template.logics:
            tmp.write('  <logic>'+eachLogic+'</logic>\r\n')
        for eachStat in template.statistics.keys():
            tmp.write('  <stat>'+eachStat+':'+str(template.statistics[eachStat])+'</stat>\r\n')
        for eachCom in template.commands:
            tmp.write('  <command>'+eachCom+'</command>\r\n')
        tmp.write('</c_template>')
        
        tmp.close()
        
        
    def loadCharTemplateFromDisk(self, t_name):
        """
        This loads a template from disk
        """
        
        template_file = MudConst.char_template_dir+t_name.capitalize()
        if os.path.isfile(template_file):
            p = make_parser()
            cth = CharTemplateHandler()
            p.setContentHandler(cth)
            p.parse(file(template_file, 'r'))
        
    def saveItemTemplateToDisk(self, template):
        """
        This pickles a template to disk.
        """
        
        template_file = MudConst.item_template_dir+os.sep+template.name.capitalize()+'.xml'
        tmp = file(template_file, 'w')
        tmp = file(template_file, 'w')
        tmp.write('<i_template name="'+template.name+'" id_num="'+str(template.id_num)+\
'" desc="'+template.desc+'">\r\n')
        for eachLogic in template.logics:
            tmp.write('  <logic>'+eachLogic+'</logic>\r\n')
        for eachStat in template.statistics.keys():
            tmp.write('  <stat>'+eachStat+':'+str(template.statistics[eachStat])+'</stat>\r\n')
        tmp.write('</i_template>')
        
        tmp.close()
        
    def loadItemTemplateFromDisk(self, t_name):
        """
        This loads a template from disk
        """
        template_file = MudConst.item_template_dir+t_name
        if os.path.isfile(template_file):
            p = make_parser()
            ith = ItemTemplateHandler()
            p.setContentHandler(ith)
            p.parse(file(template_file, 'r'))
            
            
    
    
    # Generator functions
    def generateNextId(self, type):
        if type.lower() == 'item':
            next_id = self.next_item_id + 1
            self.next_item_id = self.next_item_id + 1
            self.saveIds()
            return next_id
        if type.lower() == 'char':
            next_id = self.next_char_id + 1
            self.next_char_id = self.next_char_id + 1
            self.saveIds()
            return next_id
        if type.lower() == 'zone':
            next_id = self.next_zone_id + 1
            self.next_zone_id += 1
            self.saveIds()
            return next_id
        
    def generateCharFromTemplate(self, template_id):
        tmp = self.c_templates[int(template_id)]
        newChar = MudCharacter.MudCharacter()
        
        newChar.template_id = int(tmp.id_num)
        newChar.id_num      = self.generateNextId('char')
        newChar.name        = tmp.name
        newChar.desc        = tmp.desc
        newChar.statistics  = copy.deepcopy(tmp.statistics)
        
        for eachLogic in tmp.logics:
            newChar.addLogic(eachLogic)
        for eachCommand in tmp.commands:
            newChar.addCommand(eachCommand)
            
        return newChar

    def generateItemFromTemplate(self, template_id):
        tmp = self.i_templates[int(template_id)]
        newItem = MudItem.MudItem()
        newItem.template_id = int(tmp.id_num)
        newItem.id_num      = self.generateNextId('item')
        newItem.name = tmp.name
        newItem.desc = tmp.desc
        newItem.statistics = copy.deepcopy(tmp.statistics)
        for eachLogic in tmp.logics:
            newItem.addLogic(eachLogic)
            
        return newItem
            
    
    
    # Adding, searching, and removing functions
    def addZone(self, zone):
        """
        Adds a zone to the dictionary.
        """
        self.zones[zone.id_num] = zone
        
    def removeZone(self, zone):
        for eachChar in zone.characters.values():
            if eachChar.sockRef != '':
                eachChar.writeWithPrompt("Reality dissolved around you! Moving you to a safe area. Contact an IMM!")
                eachChar.setZone(1)
                eachChar.setRoom(1)
            else:
                zone.removeCharacter(eachChar.name)
        del self.zones[zone.id_num]
        
    def addCharacter(self, character):
        """
        Adds a Character to the world
        """
        self.characters[int(character.id_num)] = character
        
    def removeCharacter(self, character):
        """
        Removes a character from the world.
        """
        del self.characters[int(character.id_num)]
        
    def addItem(self, item):
        self.items[item.id_num] = item
        
    def removeItem(self, item):
        del self.items[item.id_num]
        
    def returnRoomRef(self, zone_id, room_id):
        """
        Returns a reference to a room instance.
        
        Takes the zone id that the room is located in, and the room id that
        you want the instance reference of.
        """
        return self.zones[zone_id].rooms[room_id]
        
    def returnZoneRef(self, zone_id):
        """
        Returns a reference to a zone. Takes a zone ID as an argument.
        """
        return self.zones[int(zone_id)]
    
    def findChar(self, id_num):
        if self.characters.has_key(int(id_num)):
            return self.characters[int(id_num)]
        else:
            return None
        
    def findCharByName(self, name):
        for eachChar in self.characters.values():
            if eachChar.name.lower() == name.lower():
                return eachChar
        return None
    
    def findCharsByName(self, name):
        tmp = []
        for eachChar in self.characters.values():
            if name.lower() in eachChar.name.lower():
                tmp.append(eachChar)
        return tmp
    def findCharTemplateByName(self, name):
        tmp = []
        for eachChar in self.c_templates.values():
            if name.lower() in eachChar.name.lower():
                tmp.append(eachChar)
        return tmp
    
    def findItem(self, id):
        if self.items.has_key(int(id)):
            return self.items[int(id)]
        else:
            return None
        
    def findItemByName(self, name):
        tmp = []
        for eachItem in self.items.values():
            if string.lower() in eachItem.name.lower():
                tmp.append(eachItem)
        return tmp
    def findItemsByName(self, string):
        tmp = []
        for eachItem in self.items.values():
            if string.lower() in eachItem.name.lower():
                tmp.append(eachItem)
        return tmp
                
    def findItemTemplateByName(self, string):
        tmp = []
        for eachItem in self.i_templates.values():
            if string.lower() in eachItem.name.lower():
                tmp.append(eachItem)
        return tmp
    
    def checkZoneNameExists(self, string):
        tmp = []
        for eachZone in self.zones.values():
            if string.lower() == eachZone.name.lower():
                return True
        return False
    
    def cleanUpCharItems(self, player):
        for eachItem in self.items.values():
            if eachItem.owner.lower() == player.name.lower():
                del self.items[eachItem.id_num]
        
    
    
    # Misc functions
    def returnRoomCharacters(self, zone_id, room_id):
        # Make this more efficient
        tmp = []
        for eachChar in self.characters.values():
            if eachChar.zone == zone_id and eachChar.room == room_id:
                tmp.append(eachChar)
        return tmp
    
    def returnRoomItems(self, zone_id, room_id):
        # Make this more efficient
        tmp = []
        for eachItem in self.items.values():
            try:
                if eachItem.zone.id_num == int(zone_id) and eachItem.room.id_num == int(room_id):
                    tmp.append(eachItem)
            except AttributeError:
                pass
        return tmp
    def returnRoomPortals(self, zone_id, room_id):
        tmp = []
        for eachPortal in self.returnRoomRef(zone_id, room_id).portals.values():
            tmp.append(eachPortal)
        return tmp
            
    def copyCharObject(self, p_tmp, p_object):
        '''
        Copies the attributes from a saved char to the new one.
        '''
        
        p_object.name       = p_tmp.name
        p_object.password   = p_tmp.password
        p_object.desc       = p_tmp.desc
        p_object.zone       = p_tmp.zone
        p_object.room       = p_tmp.room
        p_object.id_num     = p_tmp.id_num
        p_object.template_id = p_tmp.template_id
        p_object.items      = copy.deepcopy(p_tmp.items)
        p_object.statistics = copy.deepcopy(p_tmp.statistics)
        p_object.commands   = copy.deepcopy(p_tmp.commands)
        p_object.logic_modules     = copy.deepcopy(p_tmp.logic_modules)
        del p_tmp
        return p_object
    
    def isConnected(self, name):
        """
        Checks if a player is logged in.
        """

        if self.characters.has_key(name):
            return True

        return False
db = DatabaseManager()
        
        

    
