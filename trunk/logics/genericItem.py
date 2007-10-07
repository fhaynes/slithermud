import MudLogic

class genericItem(MudLogic.MudLogic):
    def __init__(self):
        MudLogic.MudLogic.__init__(self)
        
    def process(self, action, owner):
        if action.getType() == 'look':
            action.getPlayerRef().writePlain('\r\n'+owner.getName()+' is here.')