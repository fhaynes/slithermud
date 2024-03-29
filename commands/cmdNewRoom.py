"""
cmdNewRoom.py
Author: Fletcher Haynes
This file handles creating a new room. Creates a new room in the zone the
user is in.
"""

import MudCommand
import MudWorld
import MudRoom

import string

class cmdNewRoom(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "newroom"
        self.info['helpText']   = '''Creates a new room with the optionally specified name.'''
        self.info['useExample'] = '''newroom (The Room of Horrible Horror)'''
        
    def process(self, player, args=''):
        # First, let's get a reference to the zone the player is in
        z = player.getZoneRef()
        
        # Now we'll make a new room.
        newRoom = MudRoom.MudRoom()
        newRoom.setId(z.getNewId('room'))
        
        # If they supplied a name, we'll use that instead of the default.
        if args != '':
            newRoom.setName(args)

            # Now we add the room to the zone!
            z.addRoom(newRoom)
            
            # Add some initial logics
            name, logic = MudWorld.world.logicDb.getLogic('genericRoom')
            newRoom.addLogic(name, logic)
            
            # Tell the player it was created and what the ID is
            player.writeWithPrompt("Room was created with an ID of: "+str(newRoom.getId()))
            
            # And save the zone
            MudWorld.world.db.saveZone(z)
            
        else:
            player.writeWithPrompt("You must supply a room name!")
            return


        
