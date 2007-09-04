"""
This is the base MudObject class. Mobiles, players, and objects are all
derived from this class.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""
import copy
class MudObject(object):
    """
    The base class of items, players, mobiles, and portals in the MUD.
    
    All Objects in the MUD subclass this. Be default, the Object has:
        - A name
        - An ID number
        - A description
        - A dictionary holding commands words as keys, and a reference to the
          command instance as a value.
        - A dictionary holding statistics, with the statistic name as a key, and
          the statistic value as the value (for strength, or others)
        - A dictionary holding logic modules, with the module name as a key, and
          a reference to the module as the value.
    """
    
    def __init__(self):
 
         self.name   = ''
         self.desc   = ''
         self.id_num = 0

         # The commands available to an entity. The command name is the key, the
         # value is the reference to the function.
         self.commands      = {}
         
         # The various statistics for the object. Strength, etc. This will vary
         # from type to type.
         self.statistics    = {}

         # Any logic module attached to the object. Key is the name of the logic
         # module, value is a link to the module.
         self.logic_modules = {}

    ### TODO: Add try/except to catch KeyErrors ###

    # Adds a statistic to the entity. Takes the stat name, and the value. 
    def addStat(self, stat, value):
        """
        Adds a stastic along with a value to the dictionary.
        """
        if self.statistics.has_key(stat):
            return
        else:
            self.statistics[stat] = value
            return

    # Deletes a specified statistic.
    def delStat(self, stat):
        """
        Completely removes a statistic from the dictionary.
        """
        if self.statistics.has_key(stat):
            del self.statistics[stat]
        else:
            return
        
    def setStat(self, stat, value):
        if self.statistics.has_key(stat):
            self.statistics[stat] = value
        else:
            return False

    # Adds a command. Takes a command name reference to the command instance.
    def addCommand(self, command, instRef):
        """
        Adds a command and reference to the dictionary.
        """
        self.commands[command] = instRef

    # Removes a command.
    def removeCommand(self, command):
        """
        Removes a command from the dictionary.
        """
        del self.commands[command]
        
    # Imports and adds a logic module to the Object
    def addLogic(self, name):
        """
        Adds a logic module name and reference to the dictionary.
        """
        
        if not self.logic_modules.has_key(name):
            self.logic_modules[name] = copy.deepcopy(__import__(name))
            
    def removeLogic(self, name):
        """
        Removes a logic module from the dictionary.
        """
        del self.logic_modules[name]
        
    def doAction(self, action):
        """
        Queries all attached logic modules with an action instance.
        """
        for eachLogic in self.logic_modules.values():
            res = eachLogic.Execute(self, action)
            if res == 1:
                return res
        return 0
  