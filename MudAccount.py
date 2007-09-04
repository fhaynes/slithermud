"""
Holds the Account class.

@author: Jennifer Ennis
"""

import sha

class MudAccount(object):
    def _set_password(self, passwd):
        """
        Converts password to sha hex has before setting it.
        
        @param passwd: the password
        @type passwd: str
        """
        self.password = sha.new(passwd).hexdigest()
    