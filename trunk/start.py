#!/usr/bin/python

"""
Start up the MUD.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import sys
import os
import logger

import autoreload

import twisted.internet.protocol
import twisted.internet.reactor
import twisted.internet.task
import twisted.protocols.basic

import MudServer
import MudConst
import MudWorld

import profile
#import psyco
#psyco.log()
#psyco.profile()

#tick = twisted.internet.task.LoopingCall(MudWorld.world.doTick)
#tick.start(0.01)

factory = twisted.internet.protocol.Factory()
factory.protocol = MudServer.MudServer
# Should we make the port a const declared in MudConst.py?
#  Might make things a bit clearer and easier to find -V
twisted.internet.reactor.listenTCP(5003, factory)
print "Starting MUD."
MudWorld.world.loadWorld()

logger.logging.info('MUD Started.')
#autoreload.run()
#profile.Profile.bias = 4.4020750520082225e-006
#profile.run('twisted.internet.reactor.run()')
twisted.internet.reactor.run()

