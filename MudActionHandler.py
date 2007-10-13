"""
This is the Action Handler. It takes the Actions generated by the various
commands, and sends them to all the relevant logic modules. Each command
generates up to 3 actions. The first checks to see if a player *can* do
something. The second does it, and the third notifies everything that the
player did it.

@author: Fletcher Haynes
@copyright: (c)2004 Fletcher Haynes, All rights reserved.
"""
import time

import MudWorld
import MudAction
import logger

# TODO: Update docstrings to include details on what each field of
# the action should be for each action type
class MudActionHandler:
    def __init__(self):
        
        # Holds the timed actions
        self.actionQueue = []
        
        # Current time of the game (doesn't match the real world time!)
        self.gameTime    = None
        
    def doAction(self, action):
        if action.getType()   == 'say':
            self.say(action)
        elif action.getType() == 'look':
            self.look(action)
        elif action.info['actionType'] == 'vision':
            self.actionRoomCharacters(action, action.getData1())
        elif action.getType() == 'enterworld':
            self.enterWorld(action)
        elif action.getType() == 'enterportal':
            self.enterPortal(action)
        elif action.getType() == 'getitem':
            self.getItem(action)
        elif action.getType() == 'dropitem':
            self.dropItem(action)
        elif action.getType() == 'forcetransport':
            self.forceTransport(action)
        elif action.getType() == 'addstat':
            self.addStat(action)
        elif action.getType() == 'removestat':
            self.removeStat(action)
        elif action.getType() == 'modifystat':
            self.modifyStat(action)
        elif action.getType() == 'do':
            self.routeAction(action)
        elif action.getType() == 'addlogic':
            self.addLogic(action)
        elif action.getType() == 'removelogic':
            self.removeLogic(action)
        elif action.getType() == 'messagelogic':
            self.messageLogic(action)
        elif action.getType() == 'leaveworld':
            self.leaveWorld(action)
        elif action.getType() == 'spawnitem':
            self.spawnItem(action)
        elif action.getType() == 'spawncharacter':
            self.spawnCharacter(action)
        elif action.getType() == 'destroycharacter':
            self.destroyCharacter(action)
        elif action.getType() == 'destroyitem':
            self.destroyItem(action)
        else:
            pass
    
    # -------------------------------------- #
    # Functions to pass actions to multiple
    # entities of the same type. All items 
    # in a room, all portals, etc.
    # -------------------------------------- #
            
    def actionRoom(self, action, room):
        """Sends the action instance to the supplied room."""
        room.doAction(action)
        
    def actionRoomItems(self, action, room):
        """Sends the action to all the items in the supplied room."""
        for eachItem in room.getItems().values():
            eachItem.doAction(action)
            
    def actionRoomChars(self, action, room):
        """Sends the action to all the characters in the supplied room."""
        for eachChar in room.getCharacters().values():
            eachChar.doAction(action)

    def actionRoomPortals(self, action, room):
        """Sends the action to all the portals in the supplied room."""
        for eachPortal in room.getPortals().values():
            eachPortal.doAction(action)

            
    # -------------------- #
    #  Querying Functions  #
    # -------------------- #
    
    def queryZone(self, action):
        """Queries the zone of the player that generated the action."""
        action.getPlayerRef().getZoneRef().doQuery(action)
            
    def queryRoom(self, action):
        """Queries the room of the player that generated the action."""
        return action.getPlayerRef().getRoomRef().doQuery(action)
    
    def queryRoomChars(self, action):
        """
        Queries all the characters in the room of the player that generated
        the action.
        """
        for eachChar in action.getPlayerRef().getRoomRef().getCharacters().values():
            result = eachChar.doQuery(action)
            if result == 1:
                return 1
        return 0
    
    def queryRoomItems(self, action):
        """
        Queries each item in the room of the player that generated the action.
        """
        for eachItem in action.getPlayerRef().getRoomRef().getItems().values():
            result = eachItem.doQuery(action)
            if result == 1:
                return 1
        return 0
    
    def queryRoomPortals(self, action):
        """
        Queries each portal in the room of the player that generated the action.
        """
        
        for eachPortal in action.getPlayerRef().getRoomRef().getPortals().values():
            result = eachPortal.doQuery(action)
            if result == 1:
                return 1
        return 0
    
    def routeAction(self, action):
        """
        Handles custom actions.
        """
        action.getData2.doAction(action)
    
    
    
    # ------------------------------ #
    # Handlers for specific actions  #
    # ------------------------------ #
    
    def enterPortal(self, action):
        """
        Handles a character attempting to enter a portal.
        data1 is the portal they tried to enter
        """
        
        # First, we'll get some references for brevity's sake.
        
        # Character who tried to enter the portal
        c = action.getPlayerRef()
        
        # Portal the character tried to enter
        p = action.getData1()
        
        # Current room of the player
        r = c.getRoomRef()
        
        # Current zone of the player
        z = c.getZoneRef()
        
        # Now we need to get some info on where they are trying to go.
        # TODO: Error checking for invalid IDs
        newZone = MudWorld.world.getZone(p.getTargetZone())
        newRoom = newZone.getRoom(p.getTargetRoom())
        
        # Now lets check if they are trying to change zones
        if newZone.getId() == c.getZoneRef().getId():
            changeZone = False
        else:
            changeZone = True

        # If they are going to change zones, we need to do some additional
        # checks.
        
        # TODO: Are we generating too many actions? Also, should we not use
        # the queryZone function? For when we are querying just one thing,
        # should we just query it directly?
        if changeZone:
            result = self.queryZone(MudAction.MudAction("canleavezone", c, c.getZoneRef()))
            if result == 1:
                return
            
            # Now we check the destination zone to make sure they can enter.
            result = self.queryZone(MudAction.MudAction('canenterzone', c, newZone))
            if result == 1:
                return
            
            # Now let's ask the character if they can leave the zone
            result = c.doQuery(MudAction.MudAction('canleavezone', c, c.getRoomRef()))
            if result == 1:
                return
            
            # And ask the character if they can enter a new zone
            result = c.doQuery(MudAction.MudAction('canenterzone', c, newRoom))
            if result == 1:
                return
        
        # Ask the current room if they can leave it.
        result = r.doQuery(MudAction.MudAction('canleaveroom', c))
        if result == 1:
            return
        
        # Ask the new room if they can enter it.
        result = newRoom.doQuery(MudAction.MudAction('canenterroom', c))
        if result == 1:
            return
            
        # Ask the character if they can leave the room
        result = c.doQuery(MudAction.MudAction('canleaveroom', c))
        if result == 1:
            return
        
        # Ask the portal if they can enter it
        result = p.doQuery(MudAction.MudAction('canenterportal', c))
        if result == 1:
            return
        
        # If we are this point, then we know the action is ok.
        # Now, if they changed zones, we need to notify the zones.
        # TODO: Might want to use one action for this part instead of
        # generating a lot of new ones
        
        if changeZone:
            z.doAction(MudAction.MudAction('leavezone', c, z))
            newZone.doAction(MudAction.MudAction('enterzone', c, newZone))
            
        # Now we'll tell all the characters in the old room that they left.
        self.actionRoomChars(MudAction.MudAction('leaveroom', c, p), r)
        
        # Now we'll tell all the items in the old room that they left.
        self.actionRoomItems(MudAction.MudAction('leaveroom', c, p), r)
        
        # And finally we tell the old room
        r.doAction(MudAction.MudAction('leaveroom', c, p))
        
        # Now we tell the portal that they entered it
        p.doAction(MudAction.MudAction('enterportal', c))
        
        # And the character that we entered the portal
        c.doAction(MudAction.MudAction('enterportal', c))
        
        # Now it is time to do the actual mechanics of moving the character.
        # Deleting them from the old room/zone, adding them to the new ones, etc.
        if changeZone:
            # Remove char from old zone
            z.removeCharacter(c.getName())
            
            # Add to new one
            newZone.addCharacter(c)
            
        # Remove them from the old room
        r.removeCharacter(c.getName())

        # Add the character to the new room
        newRoom.addCharacter(c)
        
        # Tell everyone in the new zone that the char is entering
        if changeZone:
            newZone.doAction(MudAction.MudAction('enterzone', c))
            
            # Tell the char they are entering a new zone.
            c.doAction(MudAction.MudAction('enterzone', c))
            
        # Tell the room they entered
        newRoom.doAction(MudAction.MudAction('enterroom', c, p))
        
        # Tell the characters in the new room that the char entered
        self.actionRoomChars(MudAction.MudAction('enterroom', c, p), newRoom)
        
        # Tell all the items they entered
        self.actionRoomItems(MudAction.MudAction('enterroom', c, p), newRoom)
        
    
    def enterWorld(self, action):
        """Handles setting a player up in the world."""
        # TODO: Error checking for not finding the zone #
        MudWorld.world.addCharacter(action.getPlayerRef())
        destZone = MudWorld.world.getZone(action.getData1())
        destZone.addCharacter(action.getPlayerRef())
        destRoom = destZone.getRoom(action.getData2())
        destRoom.addCharacter(action.getPlayerRef())
        
    def leaveWorld(self, action):
        """Handles logging a character out of the world."""
        # TODO: Maybe we want to leave the player object resident in memory,
        # as that would make handling timed actions much easier.
        c = action.getPlayerRef()
        c.writeWithPrompt("Goodbye!")
        MudWorld.world.db.savePlayer(action.getPlayerRef())
        z = action.getPlayerRef().getZoneRef()
        r = action.getPlayerRef().getRoomRef()
        r.removeCharacter(c.getName())
        z.removeCharacter(c.getName())
        MudWorld.world.removeCharacter(c.getName())
        c.getSockRef().loseConnection()
        return
        
        
        
    def say(self, action):
        """Handles say actions."""
        
        action.setType('cansay')
        # First we have to check with the room to see if it is ok for them
        # to say something.
        
        result = self.queryRoom(action)
        if result == 1:
            return
        
        # Now we check all the other players in the room.
        result = self.queryRoomChars(action)
        if result == 1:
            return
            
        # Now we check all the items.
        result = self.queryRoomItems(action)
        if result == 1:
            return
        
        # If we are this point, nothing denied the action. So we change the
        # actiontype back to 'say'.
        action.setType('say')
        
        # And now we tell each relevant entity what was said.
        self.actionRoom(action, action.getPlayerRef().getRoomRef())
        self.actionRoomItems(action, action.getPlayerRef().getRoomRef())
        self.actionRoomChars(action, action.getPlayerRef().getRoomRef())

    def look(self, action):
        """Handles look actions."""

        # Adding some defactor variables here for explicity and brevity's sake
        room = action.getPlayerRef().getRoomRef()
        
        action.setType('canlook')
        
        result = self.queryRoom(action)
        if result == 1:
            return

        # Why and what are we querying the characters and items in the room for?
        # If we're looking just at the room (the default case) shouldn't the room
        # be able to query the players and items within it?  Will a look fail if
        # there's nothing in the room with the player?  What about scrying or something?
        
        # Now we check all the other players in the room.
        result = self.queryRoomChars(action)
        if result == 1:
            return
            
        # Now we check all the items.
        result = self.queryRoomItems(action)
        if result == 1:
            return
        action.setType('look')
        # I'm uncertain why we're sending the look action to all the characters
        # and items in the room?  To let them know they've been looked at?
        # Is there a better way to do this?
        self.actionRoom(action, room)
        self.actionRoomChars(action, room)
        self.actionRoomItems(action, room)
        
        action.getPlayerRef().writeWithPrompt("")
        
    def getItem(self, action):
        """
        Handles a player picking up an item from a room.
        data1 is a reference to the item they tried to get.
        data2 is the quantity they tried to get.
        """
        # Do some assignments for brevity's sake
        # Player that tried to get the item
        c = action.getPlayerRef()
        
        # The item the player tried to get
        i = action.getData1()
        
        # Get the quantity
        q = action.getData2()

        if i.isQuantity() == True and q < 1:
            c.writeWithPrompt("You cannot get less than one of an item!")
            return
        
        if i.isQuantity() == True and q > i.getQuantity():
            c.writeWithPrompt("There are not that many to get!")
            return
        

        # Now, let's make sure the item and character are in the same room still
        if i.getRoomRef().getId() != c.getRoomRef().getId():
            
            # TODO: Write some try/except code here
            return
        
        # Let's ask the item if they can get gotten
        if i.doQuery(MudAction.MudAction('cangetitem', c, i)) == 1:
            return
        
        # And let's ask the room if they can get it
        if c.getRoomRef().doQuery(MudAction.MudAction('cangetitem', c, i)) == 1:
            return
        
        # And finally we ask the character
        if c.doQuery(MudAction.MudAction('cangetitem', c, i)) == 1:
            return
        
        # So if we are at this point, we can do the physical movement required
        
        # If the player tries to get a quantity item, but the quantity they
        # want is not equal to what is in the room (i.e., someone tries to get
        # 50g from a 100g pile), we need to make a new item containing the
        # difference.
        
        if i.isQuantity() and q != i.getQuantity():
            template = MudWorld.world.templateDatabase.findTemplateById(i.getTemplateId())
            newItem = MudWorld.world.templateDatabase.createInstance('item', i.getTemplateId())
            newItem.setQuantity(q)
            i.setQuantity(i.getQuantity() - q)
        

        # Now we sound the action to the room the item was in to tell it that
        # it was picked up
        i.getRoomRef().doAction(MudAction.MudAction('getitem', c, i))
        
        # Same for the chars in the room
        self.actionRoomChars(MudAction.MudAction('getitem', c, i), c.getRoomRef())

        # And the items
        self.actionRoomItems(MudAction.MudAction('getitem', c, i), c.getRoomRef())

        # Now we remove it from the room
        i.getRoomRef().removeItem(i)
        
        # And add it to the char's item dictionar
        c.addItem(i)

    def dropItem(self, action):
        c = action.getPlayerRef()
        i = action.getData1()
        q = action.getData2()
        r = c.getRoomRef()
        
        if i.isQuantity() and q < 1:
            c.writeWithPrompt("You cannot drop that many!")
            return
        
        if i.isQuantity() and q > i.getQuantity():
            c.writeWithPrompt("You do not have that many!")
            return
        
        queryAction = MudAction.MudAction('candropitem', c, i)
        if i.doQuery(queryAction) == 1:
            return
        if r.doQuery(queryAction) == 1:
            return
        if c.doQuery(queryAction) == 1:
            return
        
        if i.isQuantity() and q != i.getQuantity():
            template = MudWorld.world.templateDatabase.findTemplateById(i.getTemplateId())
            newItem = MudWorld.world.templateDatabase.createInstance('item', i.getTemplateId())
            newItem.setQuantity(q)
            i.setQuantity(i.getQuantity() - q)
            c.removeItem(i)
            r.addItem(i)
            r.doAction(action)
            self.actionRoomChars(action, r)
            self.actionRoomItems(action, r)
            
        else:
        
            c.removeItem(i)
            r.addItem(i)
            r.doAction(action)
            self.actionRoomChars(action, r)
            self.actionRoomItems(action, r)
        
    def forceTransport(self, action):
        """
        Handles forcing a transportation of a character.
        data1 is the target zone id
        data2 is the target room id within that zone
        """        
        c = action.getPlayerRef()
        r = c.getRoomRef()
        z = c.getZoneRef()

        if z.getId() == int(action.getData1()):
            changeZone = False
            newRoom = z.getRoom(action.getData2())
        else:
            changeZone = True
            newZone = MudWorld.world.getZone(action.getData1())
            
            newRoom = newZone.getRoom(int(action.getData2()))

        
        if changeZone:
            z.removeCharacter(c.getName())
            newZone.addCharacter(c)
            
        r.removeCharacter(c.getName())
        newRoom.addCharacter(c)
        
        if changeZone:
            newAction = MudAction.MudAction('enterzone', c)
            newZone.doAction(newAction)
            c.doAction(newAction)
        
        newAction = MudAction.MudAction('enterroom', c)
        newRoom.doAction(action)
        self.actionRoomChars(action, c.getRoomRef())
        self.actionRoomItems(action, c.getRoomRef())
        
    def spawnItem(self, action):
        """
        Spawns an item from a template ID.
        data1 field is the template id.
        data2 field is the zone it should be spawned in.
        data3 is the room in the zone it should be spawned in.
        """
        if MudWorld.world.templateDb.ifTemplateExists('item', action.getData1()):
            newItem = MudWorld.world.templateDb.createInstance('item', action.getData1())
            zone = MudWorld.world.getZone(action.getData2())
            room = zone.getRoom(action.getData3())
            room.addItem(newItem)
            name, logic = MudWorld.world.logicDb.getLogic('genericItem')
            newItem.addLogic(name, logic)
        else:
            action.getPlayerRef().writeWithPrompt("Invalid template ID!")
            
    def spawnCharacter(self, action):
        """
        Spawns a character from a template ID.
        data1 field is the template ID.
        data2 field is the zone where it should be spawned.
        data3 is the room in the zone it should be spawned in.
        """
        if MudWorld.world.templateDb.ifTemplateExists('character', action.getData1()):
            newChar = MudWorld.world.templateDb.createInstance('character', action.getData1())
            zone = MudWorld.world.getZone(action.getData2())
            room = zone.getRoom(action.getData3())
            room.addCharacter(newChar)
            name, logic = MudWorld.world.logicDb.getLogic('genericPlayer')
            newChar.addLogic(name, logic)
        else:
            pass

    def destroyItem(self, action):
        """
        Destroys a specified item.
        data1 field is a reference to the item to be destroyed.
        """
        i = action.getData1()
        MudWorld.world.idDb.addFreeId('iteminstance', i.getId())
        if i.getRoomRef() == None:
            i.clearHooks()
            i.getOwner().removeItem(i)
        else:
            i.clearHooks()
            i.getRoomRef().removeItem(i)

    def destroyCharacter(self, action):
        """
        Destroys a NPC. Does not work on players!
        data field is a reference to the mob to destroy.
        """
        # Mob to destroy
        t = action.getData1()
        
        # Make sure we aren't trying to destroy a player
        if t.getSockRef() != '':
            return
        
        # Destroy each item the char has, and free their ID numbers for
        # later use.
        for eachItem in t.getItems().values():
            newAction = MudAction.MudAction('destroyitem', None, eachItem)
            self.doAction(action)
        t.clearHooks()

        t.getRoomRef().removeCharacter(t.getName())
        MudWorld.world.idDb.addFreeId('charinstance', t.getId())
        
    def addStat(self, action):
        """Adds a stat to the provided entity."""
        action.getData1().addStat(action.getData2(), action.getData3())
    
    def removeStat(self, action):
        """Removes a stat from the entity."""
        action.getData1().removeStat(action.getData2())
        
    def modifyStat(self, action):
        """Modifies a stat of the entity."""
        action.getData1().addStat(action.getData2(), action.getData3())

    def addLogic(self, action):
        """Adds a logic module to the entity."""
        try:
            name, module = MudWorld.world.logicDb.getLogic(action.getString())
            action.getData1().addLogic(action.getString())
        except KeyError:
            logger.logging.debug("A logic module was not found upon attempting to load it! \
            The name of the module was: "+action.getString()+ '. \
            The player that originated the action was: '+action.getPlayerRef.getName())

    def remLogic(self, action):
        """Removes a logic module from the entity."""
        try:
            action.getData1().removeLogic(action.getString())
        except:
            return

    def messageLogic(self, action):
        """
        Sends a text message to a specific logic module on an entity.
        """
        try:
            logic = action.getData1().getLogic(action.getData2())
            logic.process(action)
        except KeyError:
            logger.logging.debug("A message was sent to a nonexistent logic module! \
            The name of the module was: "+action.getString()+ '. \
            The player that originated the action was: '+action.getPlayerRef.getName()+' \
            The message was: '+action.getString())


    # ------------------------------------ #
    # Functions for handling timed Actions #
    # ------------------------------------ #
    
    def getTime(self):
        """
        Gets the current time
        """
        return time.time()
    
    def addActionRelative(self, action, seconds):
        """
        Adds a timed action scheduled for execution *seconds* from the current
        time.
        """
        action.setExecutionTime(self.getTime()+seconds)
        self.actionQueue.append(action)
        sort_by_attr_inplace(self.actionQueue, 'executionTime')
        print self.actionQueue
        
    def processTimedActions(self):
        
        try:
            curTime = self.getTime()
            
            if self.actionQueue[0].executionTime < curTime:
                if self.actionQueue[0].valid == True:
                    self.actionQueue[0].unhook()
                    action = self.actionQueue.pop()
                    self.doAction(action)
                    del action
                else:
                    action = self.actionQueue.pop
                    del action
            else:
                pass
        except IndexError:
            pass
            
def sort_by_attr(seq, attr):
    """
    Sort the sequence of objects by object's attribute
    Code by Yakov Markovitch.

    Arguments:
    seq  - the list or any sequence (including immutable one) of objects to sort.
    attr - the name of attribute to sort by

    Returns:
    the sorted list of objects.
    """
    import operator

    # Use the "Schwartzian transform"
    # Create the auxiliary list of tuples where every i-th tuple has form
    # (seq[i].attr, i, seq[i]) and sort it. The second item of tuple is needed not
    # only to provide stable sorting, but mainly to eliminate comparison of objects
    # (which can be expensive or prohibited) in case of equal attribute values.
    intermed = map(None, map(getattr, seq, (attr,)*len(seq)), xrange(len(seq)), seq)
    intermed.sort()
    return map(operator.getitem, intermed, (-1,) * len(intermed))

def sort_by_attr_inplace(lst, attr):
    """
    Inplace sort the list of objects by object's attribute
    Code by Yakov Markovitch.
    """
    lst[:] = sort_by_attr(lst, attr)