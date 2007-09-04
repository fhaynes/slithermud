"""
This has a few constants the mud uses.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
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

# Admin levels

player      = 1
enforcer    = 2
builder     = 3
scripter    = 4
implementor = 5

# Home directory
home_dir = os.path.abspath('/SlitherMUD')

# Zone directory
zone_dir = os.path.join(home_dir, 'zones'+os.sep)

# Location of the zone loadlist, i.e., the names of all the zones to load into
# the game
load_list = zone_dir + 'loadlist.txt'
log_dir = home_dir + os.sep + 'logs' + os.sep
player_dir = os.path.join(home_dir, 'players'+os.sep)
mob_dir   = os.path.join(home_dir, 'mobs'+os.sep)

char_template_dir = os.path.join(home_dir, 'templates'+os.sep+'characters'+os.sep)
item_template_dir = os.path.join(home_dir, 'templates'+os.sep+'items'+os.sep)
id_data_file      = os.path.join(home_dir, 'misc'+os.sep+'ids.txt')

# Adds some stuff to the PATH
sys.path.append(zone_dir)
sys.path.append(os.path.join(home_dir, 'commands'))
sys.path.append(os.path.join(home_dir, 'modules'))

greeting = '''<green>
         
          
                                             SlitherMUD\r 

                    <r><cyan>   By: Kuros
<r>\r\n'''