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
import cmdTell
import cmdImmchat

class CommandDatabase:
    def __init__(self):
        
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
        self.commands['tell'] = cmdTell.tell
        self.commands['immchat'] = cmdImmchat.immchat
        
        self.aliases = {}
        self.aliases['n'] = 'go north'
        self.aliases['s'] = 'go south'
        self.aliases['e'] = 'go east'
        self.aliases['w'] = 'go west'
        self.aliases['ne'] = 'go northeast'
        self.aliases['nw'] = 'go northwest'
        self.aliases['l'] = 'look'
        self.aliases['inv'] = 'inventory'
        self.aliases['`'] = 'say'

    def loadStdCmds(self, user):
        user.addCommand("say",  cmdSay.say)
        user.addCommand("look", cmdLook.look)
        user.addCommand("go",   cmdGo.go)
        user.addCommand("who",  cmdWho.who)
        user.addCommand("help", cmdHelp.help)
        user.addCommand("get", cmdGet.get)
        user.addCommand("quit", cmdQuit.quit)
        user.addCommand("inventory", cmdInventory.inventory)
        user.addCommand("drop", cmdDrop.drop)
        user.addCommand("give", cmdGive.give)
        user.addCommand("tell", cmdTell.tell)
    
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
        user.addCommand("immchat", cmdImmchat.immchat)
        user.addCommand("olc", cmdOlc.olc)
        
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
        user.addCommand("immchat", cmdImmchat.immchat)
        
CommandDB = CommandDatabase()