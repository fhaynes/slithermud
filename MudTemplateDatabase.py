"""
MudTemplateDatabase.py
Author: Fletcher Haynes
This is the template DB class. It manages all the templates for items
and characters in the game.
"""

class MudTemplateDatabase:
    def __init__(self):
        self.itemTemplates = {}
        self.charTemplates = {}
    
    def addTemplate(self, templateType, template):
        """Adds a template to the DB."""
        pass
    
    def removeTemplate(self, templateType, template):
        """Removes a template from the DB."""
        pass
        
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
    
    # Need code to handle ID creation and such 
    def createInstance(self, template):
        """
        Returns a copy (instance in the MUD) of the template.
        """
        return copy.deepcopy(template)
                