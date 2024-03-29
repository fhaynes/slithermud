### 10-8-2007
### Preliminary "Search" Command
### By Vopisk

import MudCommand
import MudAction
import MudWorld

from exceptions import *

class cmdSearch(MudCommand.MudCommand):
    """ This is a search command.

    For now, this command will only search for templates in the template database.
    It also only searches by name, once this is working I will expand the search
    to include things like searching for specific stats on character or item templates.

    Syntax is: search <item/char> <name>    
    """

    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "search"
        self.info['helpText']   = '''This command allows you to search through the character and item databases for an instance or a template.'''
        self.info['useExample'] = '''search item sword'''

    def process(self, player, args = ''):
        """
        This is the meat and potatoes of our search function.  First, we'll check the arguments
        to make sure that we have everything that we need, then we perform the search and either
        return the list of matching templates that are found, or we return a message that tells
        the player that no matches were found.
        """
        args = args.lower()
        try:
            objType, objName = args.split(' ', 1)
        except ValueError:
            player.writePlain("Invalid number of arguments!\r\n")
            player.writePlain("Please use the syntax: search <item/character> <name>.\r\n")
            player.writePlain("For example:  search item sword of strength \r\n")
            return
        try:
            assert objType == "item" or objType == "character"
        except AssertionError:
            player.writePlain("The first argument must be the type of object you're looking for, either character or item.\r\n")
            player.writePlain("Please use the syntax: search <item/character> <name>.\r\n")
            player.writePlain("For example:  search item template sword \r\n")
            return
        try:
            assert objName != 0
        except AssertionError:
            player.writePlain("You must specify a name to search for in the database!\r\n")
            player.writePlain("Please use the syntax: search <item/character> <name>.\r\n")
            player.writePlain("For example: search item apple \r\n")
            return   
        objList = MudWorld.world.templateDb.listTemplatesByName(objType, objName)
        try:
            assert objList[0] != 0
            ##  Put objList display code here, not done yet!
            for eachObj in objList:
                print str(eachObj.getId()), eachObj.getName()
            player.writeWithPrompt("We found some stuff, but can't display it cause I haven't written the code yet!")
        except:
            player.writeWithPrompt("Your search returned no matches!  Sorry!  Please try again...")

        
        
            