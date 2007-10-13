"""
cmdDelZone.py
Author: Fletcher Haynes
This file handles deleting a zone.
"""

import MudCommand
import MudWorld
import MudConst

import string
import os

class cmdDelZone(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "delzone"
        self.info['helpText']   = '''Deletes the zone with the supplied ID number.'''
        self.info['useExample'] = '''delzone 3'''
        
    def process(self, player, args=''):
        if args == '':
            player.writeToSelf("Please specify a zone ID.")
            return
        
        # TODO: Do some testing with the garbage module to make sure that
        # the entire zone doesn't hang around due to circular references
        # with things in the zone, like NPCs, items, rooms, etc. If this is
        # case, we may need to go through the entire zone and manually delete
        # everything.
        try:
            name = MudWorld.world.getZone(int(args)).getName()
            MudWorld.world.removeZone(int(args))
        except KeyError:
            player.writeWithPrompt("A zone with that ID does not exist.")
            
        # Now we need to rewrite the zone list file.
        # TODO: Figure out a way to rewrite the list without having an extra
        # blank line in there.
        file = open(MudConst.zoneList, 'w')
        for eachZone in MudWorld.world.getZones().values():
            file.write(eachZone.getName()+'\n')
            
        # And now we need to delete the actual zone file itself
        try:
            os.remove(MudConst.zoneDir+name+'.zne')
        except:
            return
        
        # Finally, we add the freed ID number back into the database, and save it
        MudWorld.world.idDb.addFreeId('zone', int(args))
        
        player.writeWithPrompt("Zone: "+name+" has been deleted!")
        
            

