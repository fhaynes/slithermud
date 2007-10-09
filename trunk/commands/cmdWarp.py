"""
cmdWarp.py
Author: Fletcher Haynes
This command allows admins to instantly travel from room to room.
"""

import MudCommand
import MudWorld
import MudAction

import string
import os

class cmdWarp(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "warp"
        self.info['helpText']   = '''Lets you instantly travel to a room, zone, or player.'''
        self.info['useExample'] = '''warp (zone ID) room ID or warp playername'''
        
    def process(self, player, args=''):
        argList = args.split(" ")
        if len(argList) == 1:
            # If there is one argument, then they either want to warp to a room
            # within the zone, or to a player. If it is a number, it is a room
            # if it is letters, it is a player name.
            
            if argList[0].isdigit():
                # We'll be using the forcetransport action, as it handles all the
                # required stuff to move people around.
                newAction = MudAction.MudAction('forcetransport', player, player.getZoneRef().getId(), int(argList[0]))
                MudWorld.world.actionHandler.doAction(newAction)
                player.writeWithPrompt("You warp through space.")
                return
            
            else:
                # If it isn't a digit, it is letters. i.e., a player's name. So let's look them up.
                # If there is an exception, then we couldn't them.
                try:
                    targetPlayer = MudWorld.world.findPlayerByName(argList[0])
                    newAction = MudAction.MudAction('forcetransport', player, targetPlayer.getZoneRef().getId(), \
                    targetPlayer.getRoomRef().getId())
                    MudWorld.world.actionHandler.doAction(newAction)
                    player.writeWithPrompt("You warp through space to "+targetPlayer.getName())
                    return
                except:
                    player.writeWithPrompt("Could not find player.")
                    return
            pass
            
        elif len(argList) == 2:
            if argList[0].isdigit() and argList[1].isdigit():
                newAction = MudAction.MudAction('forcetransport', player, int(argList[0]), int(argList[1]))
                MudWorld.world.actionHandler.doAction(newAction)
                player.writeWithPrompt("You warp through space.")
                return
            else:
                player.writeWithPrompt("Zone IDs and Room IDs must be numbers!")
                return
            
        else:
            player.writeWithPrompt("Please specify an optional zone ID, a room ID, or a playername.")
            return

