import MudObject
import MudProtocol
class MudCharacter(MudObject.MudObject):    
    
    def __init__(self, sockRef=''):
        
        MudObject.MudObject.__init__(self)
        self.sockRef              = sockRef
        
        self.info['roomRef']      = None
        self.info['zoneRef']      = None
        
        self.info['password']     = ''
        self.info['login_state']  = None
        
        self.info['admin_level']  = 1

        self.info['items']        = {}

        # ID of the template the character was created from
        self.info['templateId'] = None
        
        # The rank of the player. Player, Builder, Admin, etc
        self.info['rank'] = 1
        
        # Should they see color? By default, no
        self.info['color'] = False
        
        # - D20 Stats - #
        self.stats  = {}
        self.skills = {}
        self.feats  = {}
        self.stats['statistics']['intelligence'] = 0
        self.stats['statistics']['strength']     = 0
        self.stats['statistics']['dexterity']    = 0
        self.stats['statistics']['constitution'] = 0
        self.stats['statistics']['wisdom']       = 0
        self.stats['statistics']['charisma']     = 0
        


    # --------------------- #
    # d20 get/set functions #
    # --------------------- #
    
    def getSkill(self, sname):
        """Returns the requested skill."""
        return self.skills[sname]
    
    def setSkill(self, sname, svalue):
        """Sets or adds the requested skill."""
        self.skills[sname] = svalue
        
    def getFeat(self, fname):
        """Determines if the player has the specified feat."""
        if self.feats.has_key(fname):
            return True
        else:
            return False
    
    def addFeat(self, fname):
        """
        Adds a feat to the dictionary. We don't need a value for this,
        so it will just be zero.
        """
        self.feats[fname] = True
    
    def removeFeat(self, fname):
        """Removes a feat from a character."""
        del self.feats[fname]
        
        
    # ------------------- #
    #  Get/Set Functions  #
    # ------------------- #
        
    def setRoomRef(self, room):
        """Sets the room reference the char is in."""
        self.info['roomRef'] = room
        
    def getRoomRef(self):
        """Returns the room reference the char is in."""
        return self.info['roomRef']
    
    def setZoneRef(self, zone):
        """Sets the zone reference the char is in."""
        self.info['zoneRef'] = zone
        
    def getZoneRef(self):
        """Returns the zone reference that char is in."""
        return self.info['zoneRef']
    
    def getSockRef(self):
        """Returns a reference to the transport layer of the character."""
        return self.sockRef
    
    def setSockRef(self, sockRef):
        """Sets the socket reference of the character."""
        self.info['sockRef'] = sockRef
    
    def setLoginState(self, newState):
        """Sets the login state of the character."""
        self.info['login_state'] = newState
        
    def getLoginState(self):
        """Returns the login state of the character."""
        return self.info['login_state']
    
    def setPassword(self, password):
        """Sets the char's password."""
        self.info['password'] = password
        
    def getPassword(self):
        """Returns the char's password."""
        return self.info['password']

    def setAdminLevel(self, newLevel):
        """Sets the admin level of the char."""
        self.info['admin_level'] = newLevel
        
    def getAdminLevel(self):
        """Returns the admin level of the char."""
        return self.info['admin_level']
        
    def addItem(self, item):
        """Adds an item to the dictionary. Indexed by ID Number."""
        self.info['items'][item.info['id_num']] = item
        item.setOwner(self)
        
    def removeItem(self, item):
        """Removes an item from the dictionary."""
        del self.info['items'][item.getId()]
        
    def getItems(self):
        """Returns the item dictionary."""
        return self.info['items']
    
    def clearItems(self):
        """Deletes all the items in the dictionary."""
        self.info['items'] = {}
    
    def setColor(self, flag):
        """Sets the color flag to true or false."""
        self.info['color'] = flag
        
    def getColor(self):
        """Returns true/false if the char wants color."""
        return self.info['color']
        
    def findItemByName(self, name):
        """Searches for an item in char's inventory by name."""
        for eachItem in self.getItems().values():
            if eachItem.getName().lower() == name.lower():
                return eachItem
        return None
    
    def getTemplateId(self):
        """Returns the template ID."""
        return self.info['templateId']
    
    def setTemplateId(self, idNum):
        """Sets the template ID."""
        self.info['templateId'] = int(idNum)

        
    # ---------------------- #
    # Data Writing Functions #
    # ---------------------- #
        
    def prompt(self):
        """Returns a prompt to show to the user."""
        if self.getColor() == True:
            try:
                return MudProtocol.protocolHandler.processText('\r\n'+self.info['name']+'> ')
            except AttributeError:
                pass
        else:
            try:
                return MudProtocol.protocolHandler.processNoColor('\r\n'+self.info['name']+'> ')
            except AttributeError:
                pass
            
    
    def writeWithPrompt(self, data):
        """Writes a string to the socket with a prompt following."""
        if self.getColor() == True:
            try:
                self.sockRef.write(MudProtocol.protocolHandler.processText('\r\n'+data+'\r\n'+self.prompt()))
            except AttributeError:
                pass
        else:
            try:
                self.sockRef.write(MudProtocol.protocolHandler.processNoColor('\r\n'+data+'\r\n'+self.prompt()))
            except AttributeError:
                pass

    def writePlain(self, data):
        """Writes data to the socket without a prompt following."""
        if self.getColor():
            try:
                self.sockRef.write(MudProtocol.protocolHandler.processText(data))
            except AttributeError:
                pass

        else:
            try:
                self.sockRef.write(MudProtocol.protocolHandler.processNoColor(data))
            except AttributeError:
                pass
            
        
        
        