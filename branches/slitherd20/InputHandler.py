"""
This is an all-new Input Handler class.
I felt it would be better to use a separate class for handling all input
as this way we can better pass information to the appropriate place.

@author:  Adam "Vopisk" Dean
@copyright: (c)2007, Adam Dean, All Rights Reserved
"""
import MudWorld
import MudConst
import MudLogin

class InputHandler():
    """
    I've decided to make this a generic class, so that it can be over-ridden
    if we need the same functionality in another area.
    """
    def handleInput(self, player, input):
        """
        This function will actually handle the handling of the input.
        For now, if the player is not logged in, we'll pass the info
        off to MudLogin.  If the player is logged in, we'll send the
        input to the doCommand() function within MudWorld.
        """
        if player.getLoginState() != MudConst.logedIn and player.getSockRef() != '':
            MudLogin.processLogin(player, input)
            return
        if input == '':
            player.writeWithPrompt("")
            return
        argList = input.split(" ", 1)
        try:
            MudWorld.world.doCommand(player, argList[0], argList[1])
        except IndexError:
            MudWorld.world.doCommand(player, argList[0], '')

handler = InputHandler()            