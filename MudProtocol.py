"""
This is our protocol class for the MUD server. It colorizes and helps out
with formating in the OLC system.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""

import textwrap
import string
textWrapper = textwrap.TextWrapper()
def wrapText(data):
        textWrapper.width = 70
        tmp = textWrapper.fill(data)
        tmp = tmp.lstrip()
        tmp = tmp.replace("\n", "\r\n")
        return tmp
    
class ProtocolHandler:
    def __init__(self):
        self.codes = {}
        self.textWrapper = textwrap.TextWrapper(width=80)
        
        # Color codes
        self.codes['<r>']          = '\x1B[0m'
        self.codes['<bright>']     = '\x1B[1m'
        self.codes['<dim>']        = '\x1B[2m'
        self.codes['<under>']      = '\x1B[4m'
        self.codes['<blink>']      = '\x1B[5m'
        self.codes['<black>']      = '\x1B[30m'
        self.codes['<red>']        = '\x1B[31m'
        self.codes['<green>']      = '\x1B[32m'
        self.codes['<yellow>']     = '\x1B[33m'
        self.codes['<blue>']       = '\x1B[34m'
        self.codes['<magenta>']    = '\x1B[35m'
        self.codes['<cyan>']       = '\x1B[36m'
        self.codes['<white>']      = '\x1B[37m'
        self.codes['<cls>']        = '\x1B[2J'
        
        # Cursor Control Codes
        self.codes['<save>']       = '\x1B[s'
        self.codes['<restore>']    = '\x1B[u'
        self.codes['<tab>']        = '           '
        
        # Background Color Codes
        self.codes['<bgblack>']    = '\x1B[40m'
        self.codes['<bgred>']      = '\x1B[41m'
        self.codes['<bggreen>']    = '\x1B[42m'
        self.codes['<bgyellow>']   = '\x1B[43m'
        self.codes['<bgblue>']     = '\x1B[44m'
        self.codes['<bgmagenta>']  = '\x1B[45m'
        self.codes['<bgcyan>']     = '\x1B[46m'
        self.codes['<bgwhite>']    = '\x1B[47m'
        
        
    def cursorPosition(self, x, y):
        '''
        Returns the code to force the telnet cursor to row x column y.
        '''
        
        return str('\x1B['+str(x)+';'+str(y)+'f')
    
    def processText(self, data):
        '''
        Strips out color and control tags and replaces them with VT100 codes.
        '''
        for eachKey in self.codes.keys():
            data = data.replace(eachKey, self.codes[eachKey])
        return data
protocolHandler = ProtocolHandler()
