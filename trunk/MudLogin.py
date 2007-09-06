"""
Class for handling logging a player in.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import os
import copy

import MudDatabase
import MudWorld
import MudConst
import logger
import MudCommandDatabase

class LoginHandler:
    """
    Handles the logging in of a player.
    """

    def getAccountName(self, player, data):
        """
        Checks to see if the player exists, or helps create a new one.
        """
        
        
        if data.lower() == 'new':
            player.login_state = MudConst.getNewAccountName
            player.writePlain('Choose a character name: ')
            return
        if not data.isalnum():
            player.writePlain("\r\nCharacter names may only contain letters \
and numbers. Please try again: ")
            return
        else:
            char_file = MudConst.player_dir+os.sep+data.capitalize()+'.xml'
            if MudDatabase.db.isConnected(data.capitalize()):
                player.writePlain('That player is already connected! Try again: ')
                return
            if os.path.isfile(char_file):
                tmp = MudDatabase.db.loadCharFromDisk(data.capitalize())
                player = MudDatabase.db.copyCharObject(tmp, player)
                player.writePlain('\r\nPassword: ')
                player.login_state = MudConst.getAccountPassword
                
            else:
                player.writePlain("\r\nInvalid account name. Try again: ")
                    
                 

    def getAccountPassword(self, player, data):
        """
        Asks for the user's password and checks it.
        """
        if player.password == data:
            logger.logging.info(player.name+' entered the game!')
            player.writePlain('\r\nPassword accepted!\r\n')
            player.writeWithPrompt('Welcome, '+player.name)
            player.setZone(1)
            player.setRoom(1)
            player.zoneRef.addCharacter(player)
            MudDatabase.db.addCharacter(player)
            player.roomRef.addCharacter(player)
            MudCommandDatabase.CommandDB.loadStdCmds(player)
            MudDatabase.db.saveCharToDisk(player)
            player.login_state = MudConst.logedIn     
        else:
            player.writePlain('\r\nInvalid password. Try again: ')
            return

    def getNewAccountName(self, player, data):
        """
        Gets new account name if the user is creating a new one.
        """
        if not data.isalpha():
            player.writePlain('Account names must be letters or numbers. \
Try again: ')
            return
        char_file = MudConst.player_dir+os.sep+data.capitalize()+'.ply'
        if os.path.isfile(char_file):
            player.writePlain('\r\nThat name is already in use. Try again: ')
            return
        player.writePlain('Your character name will be: '+data)
        player.writePlain('\r\nIs that ok? (Y/N): ')
        player.name = data.capitalize()
        player.login_state = MudConst.confirmNewAccountName

    def confirmNewAccountName(self, player, data):
        """
        Confirms the new account name.
        """
        if data.lower() == 'y':
            player.writePlain('\r\nChoose a password: ')
            player.login_state = MudConst.getNewAccountPass
            
        elif data.lower() == 'n':
            player.writePlain('\r\nChoose a character name: ')
            player.name = ''
            player.login_state = MudConst.getNewAccountName
        else:
            player.writePlain('\r\nInvalid choice. Try again: ')
            return

    def getNewAccountPass(self, player, data):
        """
        Gets a new account password if the player is creating a new accont.
        """
        if not data.isalnum():
            player.writePlain('Passwords must contain only letters or numbers.\
                               Try again: ')
            return
        player.writePlain('Your password will be: '+data)
        player.writePlain('\r\nIs that ok? (Y/N): ')
        player.password = data
        player.login_state = MudConst.confirmNewAccountPass
     
    def confirmNewAccountPass(self, player, data):
        """
        Confirms the new password for the account.
        """
        if data.lower() == 'y':
            player.id_num = MudDatabase.db.generateNextId('char')
            player.template_id = 2
            player.setZone(1)
            player.setRoom(1)
            logger.logging.info('New character: '+player.name+'logged in.')

            player.writePlain('Character created.\r\n')
            player.writeWithPrompt('Welcome, '+player.name)
            player.zoneRef.addCharacter(player)
            MudDatabase.db.addCharacter(player)
            player.roomRef.addCharacter(player)
            MudCommandDatabase.CommandDB.loadStdCmds(player)
            player.login_state = MudConst.logedIn
            MudDatabase.db.saveCharToDisk(player)
        

        elif data.lower() == 'n':
            player.writePlain('\r\nChoose a password: ')
            player.password = ''
            player.login_state = MudConst.getNewAccountPass
            return
        else:
            player.writePlain('\r\nInvalid choice. Try again: ')
            return
        
    #def getRace(self, player, data):
    #    if data.lower() == 'elf':
    #        player.statistics['race'] = 'elf'
    #        player.login_state = MudConst.confirmGetRace
    #        player.writePlain('\r\nYou choose: Elf. Is this correct? (Y/N): ')
    #    elif data.lower() == 'human':
    #        player.statistics['race'] = 'human'
    #        player.login_state = MudConst.confirmGetRace
    #        player.writePlain('\r\nYou choose: Human. Is this correct? (Y/N): ')
    #    elif data.lower() == 'dwarf':
    #        player.statistics['race'] = 'dwarf'
    #        player.login_state = MudConst.confirmGetRace
    #        player.writePlain('\r\nYou choose: Dwarf. Is this correct? (Y/N): ')
    #    else:
    #        player.writePlain("\r\nInvalid choice! Try again: ")
    #
    #def confirmGetRace(self, player, data):
    #    if data.lower() == 'y':
    #        if player.statistics['race'] == 'human':
    #            tmp2 = player.name
    #            tmp3 = player.password
    #            tmp = MudDatabase.db.generateCharFromTemplate(1)
    #            player = MudDatabase.db.copyCharObject(tmp, player)
    #            player.name = tmp2
    #            player.password = tmp3
    #            player.statistics['race'] = 'human'
    #            player.statistics['a_points'] = 15
    #            player.login_state = MudConst.getStats
    #            self.displayStats(player)
    #        elif player.statistics['race'] == 'elf':
    #            tmp2 = player.name
    #            tmp3 = player.password
    #            tmp = MudDatabase.db.generateCharFromTemplate(2)
    #            player = MudDatabase.db.copyCharObject(tmp, player)
    #            player.name = tmp2
    #            player.password = tmp3
    #            player.statistics['race'] = 'elf'
    #            player.statistics['a_points'] = 15
    #            player.login_state = MudConst.getStats
    #            self.displayStats(player)
    #        elif player.statistics['race'] == 'dwarf':
    #            tmp2 = player.name
    #            tmp3 = player.password
    #            tmp = MudDatabase.db.generateCharFromTemplate(3)
    #            player = MudDatabase.db.copyCharObject(tmp, player)
    #            player.name = tmp2
    #            player.password = tmp3
    #            player.statistics['race'] = 'human'
    #            player.statistics['a_points'] = 15
    #            player.login_state = MudConst.getStats
    #            self.displayStats(player)
    #
    #
    #
    #    elif data.lower() == 'n':
    #        player.login_state = MudConst.getRace
    #        player.writePlain("Please choose your race: \r\n")
    #        player.writePlain("[Elf] \r\n")
    #        player.writePlain("[Human] \r\n")
    #        player.writePlain("[Dwarf] \r\n")
    #        player.writePlain("Your choice: ")
    #        
    #    else:
    #        player.writePlain("Please choose Y or N!\r\nYour choice: ")
    #        

    #def getStats(self, player, data):
    #    if data == 'done':
    #        if player.statistics['a_points'] != 0:
    #            player.writePlain("You still have more points to spend!")
    #            return
    #        player.setZone(1)
    #        player.setRoom(1)
    #        logger.logging.info('New character: '+player.name+'logged in.')
    #        MudDatabase.db.saveCharToDisk(player)
    #        player.writePlain('Character created.\r\n')
    #        player.writeWithPrompt('Welcome, '+player.name)
    #        player.zoneRef.addCharacter(player)
    #        MudDatabase.db.addCharacter(player)
    #        player.roomRef.addCharacter(player)
    #        MudDatabase.db.loadStdCmds(player)
    #        player.login_state = MudConst.logedIn
    #        return
    #        
    #    args = data.split(" ")
    #    if len(args) != 3:
    #        player.writePlain("Proper format is: str/dex/sta/spi/int add/sub amount!!!\r\n")
    #        self.displayStats(player)
    #        return
    #        
    #
    #    elif args[1] == 'add':
    #        if not args[2].isdigit():
    #            player.writePlain('Amount must be numbers only!\r\n')
    #            return
    #            
    #        if player.statistics['a_points'] < int(args[2]):
    #            player.writePlain("You do not have that many points!\r\nYour choice: ")
    #            self.displayStats(player)
    #            return
    #        else:
    #            stat = args[0].lower()
    #            try:
    #                player.statistics[stat] += int(args[2])
    #                player.statistics['a_points'] -= int(args[2])
    #                self.displayStats(player)
    #            except:
    #                player.writePlain("Invalid statistic!\r\n>>")
    #        
    #    elif args[1] == 'sub':
    #        if not args[2].isdigit():
    #            player.writePlain('Amount must be numbers only!\r\n')
    #            return
    #        else:
    #            stat = args[0].lower()
    #            try:
    #                if player.statistics[stat] - int(args[2]) < 1:
    #                    player.writePlain("You cannot subtract that many points!\r\nYour choice:")
    #                    
    #                    return
    #                else:
    #                    player.statistics[stat] -= int(args[2])
    #                    player.statistics['a_points'] += int(args[2])
    #                    self.displayStats(player)
    #            except:
    #                player.writePlain("Invalid statistic!\r\n>>")
    #
    #    else:
    #        player.writePlain("Proper format is: str/dex/sta/spi/int add/sub amount!\r\n")
    #        self.displayStats(player)
    #        return
            
        
    def processLogin(self, player, data):
        """
        Decides which function to call based on the user's login state.
        
        Calls the appropiate function.
        """
        if player.login_state == MudConst.getAccountName:
            self.getAccountName(player, data)
        elif player.login_state == MudConst.getAccountPassword:
            self.getAccountPassword(player, data)
        elif player.login_state == MudConst.getNewAccountName:
            self.getNewAccountName(player, data)
        elif player.login_state == MudConst.getNewAccountPass:
            self.getNewAccountPass(player, data)
        elif player.login_state == MudConst.confirmNewAccountName:
            self.confirmNewAccountName(player, data)
        elif player.login_state == MudConst.confirmNewAccountPass:
            self.confirmNewAccountPass(player, data)
        #elif player.login_state == MudConst.getRace:
        #    self.getRace(player, data)
        #elif player.login_state == MudConst.confirmGetRace:
        #    self.confirmGetRace(player, data)
        #elif player.login_state == MudConst.getStats:
        #    self.getStats(player, data)
        else:
            pass
        
    
    #def displayStats(self, player):
    #    player.writePlain('\r\n\r\n')
    #    player.writePlain('Strength    : '+str(player.statistics['str'])+'\r\n')
    #    player.writePlain('Intelligence: '+str(player.statistics['int'])+'\r\n')
    #    player.writePlain('Dexterity   : '+str(player.statistics['dex'])+'\r\n')
    #    player.writePlain('Stamina     : '+str(player.statistics['sta'])+'\r\n')
    #    player.writePlain('Spirit      : '+str(player.statistics['spi'])+'\r\n')
    #    player.writePlain('Points left : '+str(player.statistics['a_points'])+'\r\n\r\n')
    #    player.writePlain('Type the first three letters of the stat, add/sub, and amount.\r\n')
    #    player.writePlain('Type done when you are done.\r\n')
    #    player.writePlain('Your choice: ')
    ## This loads standard commands, such as look, say, etc
    

loginHandler = LoginHandler()
