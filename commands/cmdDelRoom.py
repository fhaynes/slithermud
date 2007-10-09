"""
cmdDelRoom.py
Author: Fletcher Haynes
This commands handle deleting a room from a zone the user is in.
"""

import MudCommand
import MudWorld
import MudRoom

import string

class cmdDelRoom(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "delroom"
        self.info['helpText']   = '''Creates a new room with the specified ID.'''
        self.info['useExample'] = '''newroom 3'''
        
    def process(self, player, args=''):
        # First, let's get a reference to the zone the player is in
        # TODO: Look at possible memory leak issues due to characters in the
        # room having references to it.

        z = player.getZoneRef()
        
        # Now, let's remove the room from the zone.
        try:
            # Let's make sure there are no PCs in it
            for eachChar in z.getRoom(int(args)):
                if eachChar.getSockRef() != '':
                    player.writeWithPrompt("A player is in that room. Cannot proceed!")
                    return
            # If not, let's remove the room
            z.removeRoom(int(args))
            
            # And let's add the freed ID to the zone...
            z.addFreeId(args)
            player.writeWithPrompt("Room deleted!")
            return
        except KeyError:
            # If the room doesn't exist...
            player.writeWithPrompt("A Room with that ID does not exist.")
            return

        