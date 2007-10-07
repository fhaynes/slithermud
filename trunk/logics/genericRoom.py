import MudLogic

class genericRoom(MudLogic.MudLogic):
    def __init__(self):
        MudLogic.MudLogic.__init__(self)

    def process(self, action, owner):
        if action.getType() == 'look':
            c = action.getPlayerRef()
            c.writePlain('['+owner.getName()+']\r\n')
            c.writePlain(owner.getDesc()+'\r\n')
            for eachExit in owner.getPortals().values():
                c.writePlain('['+eachExit.getName()+'] ')