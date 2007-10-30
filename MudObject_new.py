"""
MudObject.py

This is the default object for everything in the MUD.
When I say everything, I mean, literally, everything.
All objects are merely compilations of templates that
will add statistics, commands and logic modules to
define the various aspects and behaviors of the object.
Players will be specially defined by a "Hitch" class
object which will represent their server transport
connection.

Author:  Adam "Vopisk" Dean (vopisk@gmail.com)
Date  :  10/28/2007
Copyright 2007, Adam Dean, All Rights Reserved
"""
import logger
import types

class MudObject:
    """
    The object class definition
    """
    def __init__(self):
        # Base dictionaries that are common to all objects.
        # The info dictionary will contain things like name,
        # description, ID number and so on.  The stats dictionary
        # will contain information about... statistics, the actual
        # game-mechanic numbers that are needed.  Commands is a
        # dictionary that contains all of the commands that the
        # object can perform and logics is a dictionary containing
        # all of the logic modules that are attached to this object.
        self.info           = {}
        self.stats          = {}
        self.commands       = {}
        self.logics         = {}
        # Base lists that are common to all objects.
        # The hooks list is for timed actions, templates
        # is a list of templates that this object has
        # and databanks is a list of strings that
        # represent which dictionaries we want to save
        # to the database.
        self.hooks          = []
        self.templates      = []
        # Initialize the databanks list with the built-in dictionaries and lists
        # that we wish to save in the database.
        self.databanks      = ["info", "stats", "commands", "logics", "hooks", "templates"]

        # Default initializations for some variables.
        self.info['name']   = 'A generic object'
        self.info['desc']   = 'This object has not been defined yet!'
        # GUID - Globally Unique ID, this number will
        # be the objects really only unique identifier.
        self.info['GUID']   = 0


    #---------------------------#
    # Action Related Functions  #
    #---------------------------#

    def doQuery(self, action):
        """
        Sends an Action instance to each logic module attached to this
        entity.  It then returns the result of each.
        """
        for eachLogic in self.logics.values():
            result = eachLogic.process(action, self)
            if result == 1:
                return 1
        return 0

    def doAction(self, action):
        """
        Sends an Action to all the modules with no return of values
        """
        for eachLogic in self.logics.values():
            eachLogic.process(action, self)

    def addHook(self, action):
        """
        Adds a reference(or hook) to the supplied Action to the hooks
        list.
        """
        self.hooks.append(action)

    def removeHook(self, action):
        """
        Deletes a reference(or hook) for the supplied action from the
        hooks list.
        """
        del self.hooks[self.hooks.index(action)]

    def clearHooks(self):
        """
        Clears all hooks from the self.hooks list.
        """
        for hook in self.hooks:
            hook.setValid(False)
            del hook

    #-------------------#
    # Get/Set Functions #
    #-------------------#

    def getID(self):
        """
        Return the GUID of the object
        """
        return self.info['GUID']

    def setID(self, number):
        """
        Set the GUID of the object
        """
        self.info['GUID'] = number

    def getName(self):
        """
        Return the name of the object
        """
        return self.info['name']

    def setName(self, string):
        """
        Set the name of the object
        """
        self.info['name'] = string

    def getDesc(self):
        """
        Return the description of the object
        """
        return self.info['desc']

    def setDesc(self, string):
        """
        Set the description of the object
        """
        self.info['desc'] = string

    #***-----------------------------------------------***#
    # Generic Get/Set/Has functions for unknown Databanks #
    #***-----------------------------------------------***#
    """
    Please note that the specific get/set and other utility
    functions defined below will be much faster than these.
    So please use those as often as possible.
    """
    def get(self, name):
        """
        Generic get function.  This will search through all
        of the entries in the databanks list to find the
        variable specified, will return None if the item
        is not found.
        """
        banks = []
        # Populate the banks list with all of the actual
        # data attributes found in the databanks list.
        for item in self.databanks:
            try:
                banks.append(getattr(self, item))
            except:
                pass
        for entry in banks:
            if type(entry) == types.DictType:
                if entry.has_key(name):
                    return entry[name]
                else:
                    pass
            elif type(entry) == types.ListType:
                if entry.count(name) > 0:
                    return entry[entry.index(name)]
                else:
                    pass
            else:
                return None

    def has(self, name):
        """
        has Function
        This generic function will search through the entire contents
        of every databank and return a true/false value depending upon
        whether we found it or not.
        """
        banks = []
        found = False
        for item in self.databanks:
            try:
                banks.append(getattr(self, item))
            except:
                pass
        for entry in banks:
            if type(entry) == types.DictType:
                if entry.has_key(name):
                    found = True
                else:
                    pass
            elif type(entry) == types.ListType:
                if entry.count(name) > 0:
                    found = True
                else:
                    pass
        return found

    def set(self, varName, varValue, databankName):
        """
        set Function
        This generic set function will set the value of
        a variable specified by the varName argument and
        give it the value of the varValue argument and insert
        that value into the databank specified by the
        databankName argument.  Note:  This function will
        only work properly with dictionaries for the time
        being.
        """
        # First, we'll make sure that databank exists...
        if hasattr(self, databankName):
            # Okay, the databank exists, let's set the value
            # but first, we'll want to double-check that the
            # databank is in fact a dictionary.
            if type(getattr(self, databankName)) == types.DictType:
                databank = getattr(self, databankName)
                databank.__setitem__(varName, varValue)
                return
            else:
                # Should probably do some error messaging here
                pass
                

    ###------------------------------------------###
    ##  Get/Set Functions for Built-In Databanks  ##
    ###------------------------------------------###

    #*** Stat Functions ***#        

    def addStat(self, name, value = None):
        """
        addStat function
        This function will add a key/value pair to the
        stats dictionary that is built-in with every
        object.  First, we'll check to see if the key
        already exists, if it does, we'll return and
        print some message saying as much, if it doesn't
        exist... we'll create it and initialize its value
        to that specified in the arguments, default is None
        if no value is given.
        """
        if self.stats.has_key(name):
            """
            Key exists, tell the user and return
            """
            logger.logging.info("Attempted to add an existing key: [%s] to object: [%d]" % (name, self.info["GUID"]))
            print "INFO: Attempted to add an existing key: [%s] to object: [%d]" % (name, self.info["GUID"])
            return
        else:
            """
            Key does not exist, create the key and assign value to it
            """
            self.stats[name] = value
            return

    def setStat(self, name, value):
        """
        setStat function
        This function will set the value of an existing key
        in the stats dictionary. If the key does not exist
        we'll report an error and return from the function.
        If the key does exist, we will override it's value
        with the new value specified in the arguments.
        """
        if self.stats.has_key(name):
            """
            Key exists, set the value of the key to the new value
            specified in the arguments.
            """
            self.stats[name] = value
            return
        else:
            """
            Key does not exist, send a message and return
            """
            logger.logging.info("Attempted to set the value of a non-existant key: [%s] to object: [%d]" % (name, self.info["GUID"]))
            print "INFO:  Attempted to add an existing key: [%s] to object: [%d]" % (name, self.info["GUID"])
            return

    def removeStat(self, name):
        """
        removeStat function
        This function will remove a stat from the built-in
        stats dictionary.
        """
        del self.stats[name]

    def getStat(self, name):
        """
        getStat function
        This function will return the value of a given key
        from the built-in stats dictionary.
        """
        if self.stats.has_key(name):
            """
            Okay, we know the key exists, return the value
            """
            return self.stats[name]
        else:
            """
            Key does not exist, return a message
            """
            logger.logging.info("Attempted to get the value of a non-existant key: [%s] from object: [%d]" % (name, self.info["GUID"]))
            print "INFO:  Attempted to get the value of a non-existant key: [%s] from object: [%d]" % (name, self.info["GUID"])
            return

    def hasStat(self, name):
        """
        hasStat function
        This function will return a simple true/false value
        based upon the presence of a specified key.
        """
        return self.stats.has_key(name)

    #*** Command Functions ***#    

    def addCommand(self, cmdName, cmdInst):
        """
        addCommand function
        This function will add a command to the built-in commands
        dictionary in the form of commands[name] = instance
        """
        if self.commands.has_key(cmdName):
            """
            The key already exists, we probably don't want to override it.
            """
            logger.logging.info("Attempted to add an existing command: [%s] to object: [%d]" % (cmdName, self.info["GUID"]))
            print "INFO:  Attempted to add an existing command: [%s] to object: [%d]" % (cmdName, self.info["GUID"])
            return
        else:
            self.commands[cmdName] = cmdInst

    def removeCommand(self, command):
        """
        removeCommand function
        This function will remove a command from the built-in
        commands dictionary.
        """
        if self.commands.has_key(command):
            """
            Okay, we have that command in the dictionary let's remove it.
            """
            del self.commands[command]
            return
        else:
            """
            We don't have that command, this will throw an error if we try
            to delete it.  So let's print a message and return instead.
            """
            logger.logging.info("Attempted to remove a non-existant command: [%s] from object: [%d]" % (command, self.info["GUID"]))
            print "INFO:  Attempted to remvoe a non-existant command: [%s] from object: [%d]" % (command, self.info["GUID"])
            return

    def getCommands(self):
        """
        getCommands function
        This function will return a list of all the command names
        """
        return self.commands.keys()

    def hasCommand(self, command):
        """
        hasCommand function
        This function will return a true/false value based upon
        the presence of a specified command in the built-in
        commands dictionary.
        """
        return self.commands.has_key(command)

    #*** Logic Module Functions ***#    

    def addLogic(self, name, instance):
        """
        addLogic function
        This function will add a logic module instance to the
        built-in logics dictionary.
        """
        if self.logics.has_key(name):
            """
            We've found an existing logic module with that name
            we don't want to add the new one.
            """
            logger.logging.info("Attempted to add an existing logic module: [%s] to object: [%d]" % (name, self.info["GUID"]))
            print "INFO:  Attempted to add an existing logic module: [%s] to object: [%d]" % (name, self.info["GUID"])
            return
        else:
            """
            Okay, that logic module doesn't exist, let's add it.
            """
            self.logics[name] = instance
            return

    def removeLogic(self, name):
        """
        removeLogic function
        This function will remove a logic module instance from
        the built-in logics dictionary.
        """
        if self.logics.has_key(name):
            """
            Okay, we have that logic module, let's get rid of it
            """
            del self.logics[name]
            return
        else:
            """
            That logic module doesn't exist, trying to delete it will return
            an error, so let's send a message instead.
            """
            logger.logging.info("Attempted to remove a non-existant logic module: [%s] from object: [%d]" % (name, self.info["GUID"]))
            print "INFO:  Attempted to remove a non-existant logic module: [%s] from object: [%d]" % (name, self.info["GUID"])
            return

    def getLogic(self, name):
        """
        getLogic function
        This function will return the module instance specified
        by name if the module exists, it will spit out a message
        otherwise.
        """
        if self.logics.has_key(name):
            """
            Okay, the logic module exists, let's return it.
            """
            return self.logics[name]
        else:
            """
            The module doesn't exist, let's return a message instead
            of an error.
            """
            logger.logging.info("Attempted to get a non-existant logic module: [%s] from object: [%d]" % (name, self.info["GUID"]))
            print "INFO:  Attempted to remove a non-existant logic module: [%s] from object: [%d]" % (name, self.info["GUID"])
            return

    def getLogicModules(self):
        """
        getLogicModules function
        This function will return all of the actual module instances on an object.
        """
        return self.logics.values()

    def getLogics(self):
        """
        getLogics function
        This function will return all of the logics modules attached to
        the object by name (the keys of the dictionary).
        """
        return self.logics.keys()

    def hasLogic(self, name):
        """
        hasLogic function
        This function will return a true/false value based upon the
        presence of a logic module on the object.
        """
        return self.logics.has_key(name)