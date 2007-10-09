import logger
import sys
import traceback
import time

import MudConst
import MudLogin
import MudCommandDatabase
import MudActionHandler
import MudDatabase
import MudLogicDatabase
import MudIdDatabase
import MudTemplateDatabase

class MudWorld:
    """
    This class contains all of the relevant data about the world.
    
    It contains a dictionary of zones, connected players, and it also handles
    input processing.    
    """
    
    def __init__(self):
        self.info = {}
        self.info['players'] = {}
        self.info['zones']   = {}
        
        # Database of commands, used for instantiating new ones for items
        # and/or characters
        self.cmdDb = MudCommandDatabase.CommandDatabase()
        
        # Class that handles all the action processing of the MUD.
        self.actionHandler = MudActionHandler.MudActionHandler()
        
        # General database class
        self.db = MudDatabase.MudDatabase()
        
        # Database of logic modules
        self.logicDb = MudLogicDatabase.LogicModuleDatabase()
        
        # ID Database
        self.idDb    = MudIdDatabase.MudIdDatabase()
        
        # Item and Char Template Database
        self.templateDb = MudTemplateDatabase.MudTemplateDatabase()
        
    # This function is responsible for loading all of the zones and the 
    # logic modules. All zones are listed in zone_index.txt and all logic
    # modules are listed in logic_index.txt.
        
    def loadWorld(self):
        """Function responsible for loading the entire world."""
        print "Loading Logic Modules..."
        
        print "Loading ID Database..."
        self.idDb = self.db.loadIdDatabase()

        print "Loading Template Database..."
        self.templateDb = self.db.loadTemplateDatabase()
        
        print "Starting Zone Loading..."
        zFile = open(MudConst.zoneList)
        for eachLine in zFile.readlines():
            try:
                eachLine = eachLine.replace('\r', '')
                eachLine = eachLine.replace('\n', '')
                print "     Loading Zone: "+eachLine
                self.addZone(self.db.loadZone(eachLine))
            except:
                pass
                
            
        print "Loading Time and Timer Database..."
        self.actionHandler.gameTime = self.db.loadGameTime()            
        
        print "MUD Started!"
        
    def processAction(self, action):
        """Sends the action to the actionHandler instance for processing."""
        self.actionHandler.doAction(action)

    def addCharacter(self, player):
        """Adds a player to the global dictionary."""
        self.info['players'][player.info['name']] = player
        
    def addZone(self, zone):
        """Adds a zone to the world."""
        self.info['zones'][zone.getId()] = zone
        
    def removeZone(self, zoneId):
        """Removes a zone from the game, based on it's ID."""
        # TODO: try/except for invalid name
        del self.info['zones'][zoneId]

    def getZone(self, zone_id):
        """Gets a reference to a zone. Takes the ID of the zone."""
        return self.info['zones'][zone_id]
    
    def getZones(self):
        """Returns the entire zone dictionary."""
        return self.info['zones']
    
    def handleInput(self, player, input):
        """
        Handles player input. If the player is not logged in, hands it off
        to the login processor in MudLogin. If they are, checks the input,
        splits it as appropiate, and sends it to doCommand.
        """
        if player.getLoginState() != MudConst.logedIn and player.getSockRef() != '':
            MudLogin.processLogin(player, input)
            return
        if input == '':
            player.writeWithPrompt("")
            return
        argList = input.split(" ", 1)
        try:
            self.doCommand(player, argList[0], argList[1])
        except IndexError:
            self.doCommand(player, argList[0], '')

    def doCommand(self, player, cmd, args):
        """
        Checks the command for validity in the command dictionary of the player
        If it is not there, notifies the player. Also catches any major errors
        while processing the command.
        """
        
        #try:
        player.info['commands'][cmd.lower()].process(player, args)
        #except KeyError:
        #    player.writeWithPrompt("Invalid command!")

##        except:
##            player.writeWithPrompt("There has been an error processing your command. Please report this to an IMM.")
##            etype = sys.exc_info()[0]
##            evalue = sys.exc_info()[1]
##            etb = traceback.extract_tb(sys.exc_info()[2])
##            string = 'Error type: '+str(etype) + '\r\nError value: '+str(evalue)+'\r\n Traceback:'+str(etb)
##            
##            logger.logging.debug(string)
            
    def getPlayers(self):
        """Returns the global player dictionary."""
        return self.info['players']
    
    def findPlayerByName(self, name):
        """Returns a reference to the player specified in name."""
        return self.info['players'][name]
            
    
            
world = MudWorld()