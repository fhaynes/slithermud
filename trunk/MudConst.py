"""
This has a few constants the mud uses.

@author: Fletcher Haynes
@copyright: (c)2007 Fletcher Haynes, All rights reserved.
"""

import sys
import os

# Connection States

getAccountName        = 1
getAccountPassword    = 2
getNewAccountName     = 3
getNewAccountPass     = 4
confirmNewAccountName = 5
confirmNewAccountPass = 6
getRace               = 7
confirmGetRace        = 8
getStats              = 9
logedIn               = 10
inOlc                 = 11

# Admin levesl

player      = 1
enforcer    = 2
builder     = 3
scripter    = 4
implementor = 5

port = 5003

# Home directory
homeDir = os.path.abspath('/Slither2')

# Zone directory
zoneDir = os.path.join(homeDir, 'zones'+os.sep)

# Location of the zone loadlist, i.e., the names of all the zones to load into
# the game
zoneList = zoneDir + 'zone_index.txt'

# Logic Directory
logicDir = homeDir+ os.sep + 'logics' + os.sep
logicIndex = logicDir + 'logic_index.txt'

playerDir = homeDir + os.sep + 'players' + os.sep

log_dir = homeDir + os.sep + 'logs' + os.sep


# Adds some stuff to the PATH
sys.path.append(zoneDir)
sys.path.append(os.path.join(homeDir, 'commands'))
sys.path.append(os.path.join(homeDir, 'logics'))

greeting = '''<green>
         
          
                    SlitherMUD\r 

                    <r><cyan>   By: Kuros
<r>\r\n'''