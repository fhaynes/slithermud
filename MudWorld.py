"""
Contains the world class for the MUD.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""



import string
import os
import sys, traceback

import MudDatabase
import MudProtocol
import MudConst
import MudLogin
import MudZone
import MudOlc
import MudAction
import MudActionHandler
import MudCommandDatabase
import logger

import time
class World:
    """
    Object containing the entire MUD World.
    
    Contains the following:
    - Dictionary of all characters logged in. Character name is the key, instance
      reference is the value.
    - Dictionary of all zones in the MUD. Zone ID is the key, instance
      reference is the value.
    - A reference to the login handler instance. Change this to use a
      custom one.
    """
    def __init__(self):
        # These are the references to a couple of classes that handle certain
        # things within the game world such as logging in, OLC, and the
        # saving/loading of players and the world. They are set with the
        # various functions in the world class.
        self.loginHandler    = MudLogin.loginHandler
        self.olcHandler      = MudOlc.OlcManager
        self.databaseHandler = MudDatabase.db
        self.protocolHandler = MudProtocol.protocolHandler
        
    def doTick(self):
        for eachChar in MudDatabase.db.characters.values():
            eachChar.ticks_since_last_input += 1
        action = MudAction.MudAction()
        action.actionType = 'tick'
        MudActionHandler.actionHandler.doAction(action)
        
    def handleInput(self, player, input):
        player.ticks_since_last_input = 0
        if player.login_state == MudConst.inOlc:
            self.olcHandler.handleInput(player, input)
            return
        if player.login_state != MudConst.logedIn and player.sockRef != '':
            self.handleLogin(player, input)
            return
        if input == '':
            player.writeWithPrompt("")
            return
        arg_list = input.split(" ", 1)
        try:
            self.doCommand(player, arg_list[0], arg_list[1])
        except IndexError:
            self.doCommand(player, arg_list[0], '')
            
        
    def doCommand(self, player, cmd, args):
        try:
            player.commands[cmd.lower()].Process(player, args)
        except KeyError:
            x = self.checkAliases(cmd)
            if x == None:
                player.writeWithPrompt("Invalid command.")
            else:
                input_string = x+' '+args
                print input_string
                self.handleInput(player, input_string)
        except:
            player.writeWithPrompt("There has been an error processing your command. Please report this to an IMM.")
            etype = sys.exc_info()[0]
            evalue = sys.exc_info()[1]
            etb = traceback.extract_tb(sys.exc_info()[2])
            string = 'Error type: '+str(etype) + '\nError value: '+str(evalue)+'\n Traceback:'+str(etb)
            logger.logging.debug(string)
    
    def checkAliases(self, cmd):
        for eachAlias in MudCommandDatabase.CommandDB.aliases.keys():
            if eachAlias == cmd.lower():
                return MudCommandDatabase.CommandDB.aliases[eachAlias]
        return None
    
    def sendToImms(self, msg):
        for eachPlayer in MudDatabase.db.characters.values():
            if eachPlayer.admin_level > 1 and eachPlayer.sockRef != '':
                eachPlayer.writeWithPrompt(msg)
                
    
    def loadTemplates(self):
        print "Loading templates..."
        self.loadItemTemplates()
        self.loadCharTemplates()
        
    def loadItemTemplates(self):
        for eachTemplate in os.listdir(MudConst.item_template_dir):
            MudDatabase.db.loadItemTemplateFromDisk(eachTemplate)
            
    def loadCharTemplates(self):
        for eachTemplate in os.listdir(MudConst.char_template_dir):
            MudDatabase.db.loadCharTemplateFromDisk(eachTemplate)
            
    def loadMobs(self):
        print "Loading MOBs..."
        for eachMob in os.listdir(MudConst.mob_dir):
            if '.xml' in eachMob:
                tmp = MudDatabase.db.loadMobFromDisk(eachMob)
                tmp.zoneRef.addCharacter(tmp)
                tmp.roomRef.addCharacter(tmp)
                MudDatabase.db.addCharacter(tmp)
            else:
                pass
            
    def loadWorld(self):
        """
        Helper function to load the entire world.
    
        All zones to be loaded must have an entry in the loadlist file.
        """
    
        f = open(MudConst.load_list, 'r')
        for eachLine in f.readlines():
            eachLine = eachLine.replace("\n", "")
            self.loadZone(eachLine)
        self.initializeOlc()
        self.initializeLoginHandler()
        self.initializeProtocolHandler()
        self.initializeDatabaseHandler()
        self.loadTemplates()
        self.loadMobs()
        MudDatabase.db.loadIds()
        
    def loadZone(self, zname):
        """
        Loads a single zone.
        
        Takes the zone name to load as an argument. It then constructs the
        directory path for the zone, and appends it to the path so we can
        load logic modules from it.
        
        Creates a new instance of MudZone and assigns it to the proper values
        from the db, and appends it to the zone dictionary.
        """
        zone_dir = MudConst.zone_dir + zname+os.sep

        # Now lets add the zone directory to the path so we can load logic
        # modules from it.
        sys.path.append(zone_dir)

        z_file   = zone_dir+zname+'.xml'
        print "Loading Zone: "+zname
        if os.path.isfile(z_file):

            # We need an empty zone instance for the data to be loaded into.
            newZone = MudDatabase.db.loadZoneFromDisk(zname)

            # And finally, append the zone. 
            MudDatabase.db.addZone(newZone)
            
        else:
            print "Error loading: "+zname
        
        

    def handleLogin(self, player, data):
        """
        Calls the login processor function if a player is not in the game.
        """
        self.loginHandler.processLogin(player, data)
        
    def initializeOlc(self):
        print "Initializing OLC system..."
        self.olcHandler = MudOlc.OlcManager()
    def initializeLoginHandler(self):
        print "Initializing Login system..."
        self.loginHandler = MudLogin.loginHandler
    def initializeProtocolHandler(self):
        print "Initializing Protocol system..."
        self.protocolHandler = MudProtocol.protocolHandler
    def initializeDatabaseHandler(self):
        self.databaseHandler = MudDatabase.db
world = World()