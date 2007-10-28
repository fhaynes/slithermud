"""
cmdNewZone.py
Author: Fletcher Haynes
This file handles created a new zone.
"""

import MudCommand
import MudWorld
import MudZone
import MudRoom
import MudConst

import string

class cmdNewZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "newzone"
        self.info['helpText']   = '''Creates a new zone with the supplied name'''
        self.info['useExample'] = '''newzone The Deadly Forest of Death'''
        
    def process(self, player, args=''):
        if args == '':
            player.writeToSelf("Please specify a zone name.")
            return
        
        # TODO: Check if the zone exists already? Or do we care if the zone
        # has a duplicate name, since it will always have a unique ID?

        # First we make a new zone instance, and assign it an ID and name
        newZone = MudZone.MudZone()
        newZone.setId(MudWorld.world.idDb.getNewId('zone'))
        newZone.setName(args)
        
        # Now we'll create an initial room in the zone.
        newRoom = MudRoom.MudRoom()
        newRoom.setId(newZone.getNewId)
        newZone.addRoom(newRoom)
        
        # Now we need to add the new zone to the zone index file.
        file = open(MudConst.zoneList, 'a')
        file.write('\n'+newZone.getName())
        file.close()
        
        # And finally, we save the zone to disk and add it to the world.
        MudWorld.world.db.saveZone(newZone)
        MudWorld.world.addZone(newZone)
        
        player.writeWithPrompt("Zone: "+newZone.getName()+' has been created!')
