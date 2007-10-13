"""
MudTemplateDatabase.py
Author: Fletcher Haynes
This is the template DB class. It manages all the templates for items
and characters in the game.
"""
import copy
import MudWorld
class MudTemplateDatabase:
    def __init__(self):
        self.itemTemplates = {}
        self.charTemplates = {}
    
    def addTemplate(self, templateType, template):
        """Adds a template to the DB."""
        if templateType == 'character':
            self.charTemplates[template.getId()] = template
        elif templateType == 'item':
            self.itemTemplates[template.getId()] = template
        else:
            return
            
    
    def removeTemplate(self, templateType, template):
        """Removes a template from the DB."""
        pass
        
    def ifTemplateExists(self, templateType, idNum):
        """Checks if a template exists by ID number."""
        if templateType.lower() == 'character':
            if self.charTemplates.has_key(idNum):
                return True
            else:
                return False
        elif templateType.lower() == 'item':
            if self.itemTemplates.has_key(idNum):
                return True
            else:
                return False
        else:
            # TODO: Error checking code for sending an invalid type
            return

        
    def findTemplateById(self, templateType, idNum):
        """
        Searches for and returns the template with a matchin ID Number.
        Returns None if it is not found.
        """
        try:
            if templateType.lower() == 'character':
                return self.charTemplates[idNum]
            elif templateType.lower() == 'item':
                return self.itemTemplates[idNum]
            else:
                # TODO: Error checking code for sending an invalid type
                return
        except KeyError:
            return None
        
    def findTemplateByName(self, templateType, name):
        """
        Searches through the templates by name.
        Returns None if it doesn't find it.
        """
        if templateType.lower() == 'character':
            for eachTemplate in self.charTemplates.values():
                if eachTemplate.getName().lower() == name:
                    return eachTemplate
            return None
        elif templateType.lower() == 'item':
            for eachTemplate in self.itemTemplates.values():
                if eachTemplate.getName().lower() == name:
                    return eachTemplate
            return None
        else:
            return None
        
    def listTemplatesByName(self, templateType, name):
        """
        Searches through the templates by name.
        Returns a list of all matching templates.
        Returns none if nothing is found.
        """
        if templateType.lower() == 'character':
            tmpList = []
            for eachTemplate in self.charTemplates.values():
                if eachTemplate.getName().lower() == name.lower():
                    tmpList.append(eachTemplate)
                return tmpList
        elif templateType.lower() == 'item':
            tmpList = []
            for eachTemplate in self.itemTemplates.values():
                if eachTemplate.getName().lower() == name.lower():
                    tmpList.append(eachTemplate)
                return tmpList

    def getAllTemplates(self, templateType):
        if templateType.lower() == "character":
            tmpList = []
            for template in self.charTemplates:
                tmpList.append(template)
            return tmpList
        elif templateType.lower() == "item":
            tmpList = []
            for template in self.itemTemplates:
                tmpList.append(template)
            return tmpList
    
    def createInstance(self, templateType, templateId):
        """
        Returns a copy (instance in the MUD) of the template.
        """
        if templateType.lower() == 'item':
            newItem = copy.deepcopy(self.itemTemplates[templateId])
            newItem.setId(MudWorld.world.idDb.getNewId('iteminstance'))
            newItem.setTemplateId(int(templateId))
            return newItem
            
        elif templateType.lower() == 'character':
            newChar = copy.deepcopy(self.charTemplates[templateId])
            newChar.setId(MudWorld.world.idDb.getNewId('charinstance'))
            newChar.setTemplateId(int(templateId))
            return newChar
        else:
            # TODO: Try/Except to catch invalid types. 
            return
                