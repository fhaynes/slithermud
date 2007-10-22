import os

import MudConst
import MudWorld
import MudAction
import logger
import diceutils
def getAccountName(player, data):
    """
    Checks to see if the player exists, or helps create a new one.
    """
    
    if data.lower() == 'new':
        player.setLoginState(MudConst.getNewAccountName)
        player.writePlain('Choose a character name: ')
        return

    if not data.isalpha():
        player.writePlain("\r\nCharacter names may only contain letters!")
        player.writePlain("\r\nPlease choose your name: ")
        return
    
    else:
        data = data.capitalize()
        char_file = MudConst.playerDir+os.sep+data+'.ply'
        if os.path.isfile(char_file):
            MudWorld.world.db.loadPlayer(data, player)
            player.writePlain('\r\nPassword: ')
            player.setLoginState(MudConst.getAccountPassword)
            
        else:
            player.writePlain("\r\nCharacter does not exist!")
            player.writePlain("\r\nEnter your character name: ")
            
def getAccountPassword(player, data):
    """
    Asks for the user's password and checks it.
    """
    if player.getPassword() == data:
        logger.logging.info(player.getName()+' entered the game!')
        player.writePlain('\r\nPassword accepted!\r\n')
        player.writeWithPrompt('Welcome, '+player.getName())
        player.setLoginState(MudConst.logedIn)
        newAction = MudAction.MudAction('enterworld', player, player.getZoneRef().getId(), player.getRoomRef().getId())
        MudWorld.world.actionHandler.doAction(newAction)
        
        # TODO: Come up with a better way to load initial commands. #
        if player.getName() == 'Admin' or player.getName() == 'Kuros':
            MudWorld.world.cmdDb.loadAllCommand(player)
    else:
        player.writePlain('\r\nInvalid password. Try again: ')
        return

def getNewAccountName(player, data):
    """
    Gets new account name if the user is creating a new one.
    """
    if not data.isalpha():
        player.writePlain('\r\nAccount names must be letters only!')
        player.writePlain('\r\nPlease choose a name: ')
        return
    data = data.capitalize()
    char_file = MudConst.playerDir+os.sep+'.ply'
    if os.path.isfile(char_file):
        player.writePlain('\r\nThat name is already in use!')
        player.writePlain('\r\nPlease choose a name: ')
        return
    player.writePlain('Your character name will be: '+data)
    player.writePlain('\r\nIs that ok? (Y/N): ')
    player.setName(data)
    player.setLoginState(MudConst.confirmNewAccountName)
    
def confirmNewAccountName(player, data):
    """
    Confirms the new account name.
    """
    if data.lower() == 'y':
        player.writePlain('\r\nChoose a password: ')
        player.setLoginState(MudConst.getNewAccountPass)
        
    elif data.lower() == 'n':
        player.writePlain('\r\nChoose a character name: ')
        player.setLoginState(MudConst.getNewAccountName)
    else:
        player.writePlain('\r\nPlease type Y or N: ')
        return
    
def getNewAccountPass(player, data):
    """
    Gets a new account password if the player is creating a new accont.
    """
    if not data.isalnum():
        player.writePlain('Passwords must contain only letters or numbers!')
        player.writePlain('Choose a password: ')
        return
    
    player.writePlain('Your password will be: '+data)
    player.writePlain('\r\nIs that ok? (Y/N): ')
    player.setPassword(data)
    player.setLoginState(MudConst.confirmNewAccountPass)
    
def confirmNewAccountPass(player, data):

    """
    Confirms the new password for the account.
    """
    if data.lower() == 'y':
        player.writePlain("Press any key to roll your stats.")
        player.setLoginState(MudConst.rollStats)

##        logger.logging.info('New character: '+player.info['name']+'logged in.')
##
##        player.writePlain('Character created.\r\n')
##        player.writeWithPrompt('Welcome, '+player.getName())
##        player.setLoginState(MudConst.logedIn)
##
##        newAction = MudAction.MudAction('enterworld', player, 1, 1)
##        MudWorld.world.actionHandler.doAction(newAction)
##        
##        # TODO: Come up with a better way to load initial commands. #
##        MudWorld.world.cmdDb.loadPlayerCommands(player)
##        
##        # TODO: Come up with better way to load initial logics. #
##        name, gen  = MudWorld.world.logicDb.getLogic('genericPlayer')
##        player.addLogic(name, gen)
##        
##        MudWorld.world.db.savePlayer(player)

    elif data.lower() == 'n':
        player.writePlain('\r\nChoose a password: ')
        player.setLoginState(MudConst.getNewAccountPass)
        return
    else:
        player.writePlain('\r\nInvalid choice. Try again: ')
        return

def rollStats(player, data):
    player.setStat('strength', diceutils.rollTotal(3, 6))
    player.setStat('dexterity', diceutils.rollTotal(3, 6))
    player.setStat('intelligence', diceutils.rollTotal(3, 6))
    player.setStat('wisdom', diceutils.rollTotal(3, 6))
    player.setStat('charisma', diceutils.rollTotal(3, 6))
    player.setStat('constitution', diceutils.rollTotal(3, 6))
    
    player.writePlain("Your rolled stats are:\r\n")
    player.writePlain("Strength    : "+str(player.getStat('strength'))+'\r\n')
    player.writePlain("Dexterity   : "+str(player.getStat('dexterity'))+'\r\n')
    player.writePlain("Constitution: "+str(player.getStat('constitution'))+'\r\n')
    player.writePlain("Intelligence: "+str(player.getStat('intelligence'))+'\r\n')
    player.writePlain("Wisdom      : "+str(player.getStat('wisdom'))+'\r\n')
    player.writePlain("Charisma    : "+str(player.getStat('charisma'))+'\r\n')
    player.writePlain("Are these acceptable? (Y/N) : ")
    player.setLoginState(MudConst.confirmStats)

def confirmStats(player, data):
    if data.lower() == 'y':
        logger.logging.info('New character: '+player.info['name']+'logged in.')

        player.writePlain('Character created.\r\n')
        player.writeWithPrompt('Welcome, '+player.getName())
        player.setLoginState(MudConst.logedIn)

        newAction = MudAction.MudAction('enterworld', player, 1, 1)
        MudWorld.world.actionHandler.doAction(newAction)
        
        # TODO: Come up with a better way to load initial commands. #
        MudWorld.world.cmdDb.loadPlayerCommands(player)
        
        # TODO: Come up with better way to load initial logics. #
        name, gen  = MudWorld.world.logicDb.getLogic('genericPlayer')
        player.addLogic(name, gen)
        
        MudWorld.world.db.savePlayer(player)
        return
    elif data.lower() == 'n':
        player.writePlain("\r\nPress enter to reroll your stats.")
        player.setLoginState(MudConst.rollStats)
        return
    else:
        player.writePlain("\r\nPlease type Y or N: ")
        return
        
    

def processLogin(player, data):
    """
    Decides which function to call based on the user's login state.
      
    Calls the appropiate function.
    """
    if player.getLoginState() == MudConst.getAccountName:
        getAccountName(player, data)
    elif player.getLoginState() == MudConst.getAccountPassword:
        getAccountPassword(player, data)
    elif player.getLoginState() == MudConst.getNewAccountName:
        getNewAccountName(player, data)
    elif player.getLoginState() == MudConst.confirmNewAccountName:
        confirmNewAccountName(player, data)
    elif player.getLoginState() == MudConst.getNewAccountPass:
        getNewAccountPass(player, data)
    elif player.getLoginState() == MudConst.confirmNewAccountPass:
        confirmNewAccountPass(player, data)
    elif player.getLoginState() == MudConst.rollStats:
        rollStats(player, data)
    elif player.getLoginState() == MudConst.confirmStats:
        confirmStats(player, data)
    else:
        pass