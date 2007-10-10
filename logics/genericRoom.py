import MudLogic
import MudConst

class genericRoom(MudLogic.MudLogic):
    def __init__(self):
        MudLogic.MudLogic.__init__(self)

##    def process(self, action, owner):
##        if action.getType() == 'look':
##            c = action.getPlayerRef()
##            c.writePlain('['+owner.getName()+']\r\n')
##            c.writePlain(owner.getDesc()+'\r\n')
##            for eachExit in owner.getPortals().values():
##                c.writePlain('['+eachExit.getName()+'] ')


    def process(self, action, owner):
        # Default variable for the object initiating the action
        actor = action.getPlayerRef()

        def checkWizview(actor, room):
            if actor.getAdminLevel() >= MudConst.builder and actor.getStat('wizview') == True:
                return '(' + room.getId() + ')'
            else:
                return ' '
            
        
        if action.getType() == 'look':
            doWizview = checkWizview(actor, owner)
            actor.writePlain('[' + owner.getName() + ']%s\r\n' % doWizview)
            actor.writePlain(owner.getDesc() + '\r\n')

            for eachExit in owner.getPortals().values():
                actor.writePlain('[' + eachExit.getName() + '] ')