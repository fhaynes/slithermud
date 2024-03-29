class MudCommand:
    """
    This is the base class for all commands in the MUD.
    """
    def __init__(self):
        self.info = {}
        self.info['cmdName']    = ''
        self.info['helpText']   = ''
        self.info['useExample'] = ''
        
    def setType(self, type):
        self.info['actiontype'] = type

    def getName(self):
        return self.info['cmdName']

    def getHelpText(self):
        return self.info['helpText']

    def getUseExample(self):
        return self.info['useExample']