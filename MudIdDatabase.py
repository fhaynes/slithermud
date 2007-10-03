"""
MudIdDatabase.py
Author: Fletcher Haynes
This class keeps track of all the IDs in the MUD. Which are in use, which
are free, etc. It also handles giving out free IDs when something asks for
one.
"""

class MudIdDatabase:
    def __init__(self):
        # These are the highest known ID numbers we have used for each
        # idType so far. If we don't have a free one, we have to increment
        # these by one and use that.
        self.nextItemTemplate = 1
        self.nextCharTemplate = 1
        self.nextItemInstance = 1
        self.nextCharInstance = 1
        
        # Thes are lists of IDs that come from things that have been
        # destroyed, so they are free for use again.
        self.freeItemTemplateIds = []
        self.freeCharTemplateIds = []
        self.freeItemInstanceIds = []
        self.freeCharInstanceIds = []
        
    def addFreeId(self, idType, id_num):
        """This takes an ID number and adds it to the appropiate freed list."""
        if idType.lower()   == 'itemtemplate':
            self.freeItemTemplateIds.append(int(id_num))
            self.freeItemTemplateIds.sort(reverse=True)
            
        elif idType.lower() == 'chartemplate':
            self.freeCharTemplateIds.append(int(id_num))
            self.freeCharTemplateIds.sort(reverse=True)
        elif idType.lower() == 'iteminstance':
            self.freeItemInstanceIds.append(int(id_num))
            self.freeItemInstanceIds.sort(reverse=True)            
        elif idType.lower() == 'charinstance':
            self.freeCharInstanceIds.append(int(id_num))
            self.freeCharTemplateIds.sort(reverse=True)
        else:
            # TODO some error checking code in case an invalid idType
            # is sent?
            return

    def getNewId(self, idType):
        """Will get the next available ID number for the correct idType."""
        if idType.lower() == 'itemtemplate':
            try:
                return self.freeItemTemplateIds.pop()
            except IndexError:
                nextId = self.nextItemTemplate
                self.nextItemTemplate += 1

        elif idType.lower() == 'iteminstance':
            try:
                return self.freeItemInstanceIds.pop()
            except IndexError:
                nextId = self.nextItemInstance
                self.nextItemInstance += 1

        elif idType.lower() == 'chartemplate':
            try:
                return self.freeCharTemplateIds.pop()
            except IndexError:
                nextId = self.nextCharTemplate
                self.nextCharTemplate += 1

        elif idType.lower() == 'charinstance':
            try:
                return self.freeCharInstanceIds.pop()
            except IndexError:
                nextId = self.nextCharInstance
                self.nextCharInstance += 1
        else:
            # TODO: Error checking code for an invalid idType
            pass
            