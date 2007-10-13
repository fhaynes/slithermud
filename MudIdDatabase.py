"""
MudIdDatabase.py
Author: Fletcher Haynes
This class keeps track of all the IDs in the MUD. Which are in use, which
are free, etc. It also handles giving out free IDs when something asks for
one.
"""
import MudWorld

class MudIdDatabase:
    def __init__(self):
        # These are the highest known ID numbers we have used for each
        # idType so far. If we don't have a free one, we have to increment
        # these by one and use that.
        self.nextItemTemplate = 1
        self.nextCharTemplate = 1
        self.nextItemInstance = 1
        self.nextCharInstance = 1
        self.nextZoneId       = 3
        
        # Thes are lists of IDs that come from things that have been
        # destroyed, so they are free for use again.
        self.freeItemTemplateIds = []
        self.freeCharTemplateIds = []
        self.freeItemInstanceIds = []
        self.freeCharInstanceIds = []
        self.freeZoneIds         = []
        
    def addFreeId(self, idType, idNum):
        """This takes an ID number and adds it to the appropiate freed list."""
        if idType.lower()   == 'itemtemplate':
            self.freeItemTemplateIds.append(int(idNum))
            self.freeItemTemplateIds.sort(reverse=True)
            MudWorld.world.db.saveIdDatabase()
        elif idType.lower() == 'chartemplate':
            self.freeCharTemplateIds.append(int(idNum))
            self.freeCharTemplateIds.sort(reverse=True)
            MudWorld.world.db.saveIdDatabase()
        elif idType.lower() == 'iteminstance':
            self.freeItemInstanceIds.append(int(idNum))
            self.freeItemInstanceIds.sort(reverse=True)    
            MudWorld.world.db.saveIdDatabase()        
        elif idType.lower() == 'charinstance':
            self.freeCharInstanceIds.append(int(idNum))
            self.freeCharTemplateIds.sort(reverse=True)
            MudWorld.world.db.saveIdDatabase()
        elif idType.lower() == 'zone':
            self.freeZoneIds.append(int(idNum))
            self.freeZoneIds.sort(reverse=True)
            MudWorld.world.db.saveIdDatabase()
        else:
            # TODO some error checking code in case an invalid idType
            # is sent?
            return

    # TODO: Do we want to save the ID DB every time it generates a new ID,
    # so as to ensure we have a current record saved to disk in the event
    # of a crash?
    def getNewId(self, idType):
        """Will get the next available ID number for the correct idType."""
        if idType.lower() == 'itemtemplate':
            try:
                return self.freeItemTemplateIds.pop()
            except IndexError:
                nextId = self.nextItemTemplate
                self.nextItemTemplate += 1
                return nextId

        elif idType.lower() == 'iteminstance':
            try:
                return self.freeItemInstanceIds.pop()
            except IndexError:
                nextId = self.nextItemInstance
                self.nextItemInstance += 1
                return nextId

        elif idType.lower() == 'chartemplate':
            try:
                return self.freeCharTemplateIds.pop()
            except IndexError:
                nextId = self.nextCharTemplate
                self.nextCharTemplate += 1
                return nextId

        elif idType.lower() == 'charinstance':
            try:
                return self.freeCharInstanceIds.pop()
            except IndexError:
                nextId = self.nextCharInstance
                self.nextCharInstance += 1
                return nextId
                
        elif idType.lower() == 'zone':
            try:
                return self.freeZoneIds.pop()
            except IndexError:
                nextId = self.nextZoneId
                self.nextZoneId += 1
                return nextId
        else:
            # TODO: Error checking code for an invalid idType
            pass
            