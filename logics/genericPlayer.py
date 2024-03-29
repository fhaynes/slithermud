import MudLogic

class genericPlayer(MudLogic.MudLogic):
    def __init__(self):
        MudLogic.MudLogic.__init__(self)

    def process(self, action, owner):
        if action.getType() == 'say':
            owner.writeWithPrompt(action.getPlayerRef().getName()+ ' says, "'+action.getString()+'"')
        elif action.getType() == 'enterroom':
            owner.writeWithPrompt(action.getPlayerRef().getName()+ ' enters via '+ action.getData1().getName())
        elif action.getType() == 'leaveroom':
            owner.writeWithPrompt(action.getPlayerRef().getName()+ ' exits via '+action.getData1().getName())
        elif action.getType() == 'getitem':
            owner.writeWithPrompt(owner.getName()+' gets: '+action.getData1().getName())
        elif action.getType() == 'dropitem':
            owner.writeWithPrompt(owner.getName()+' drops: '+action.getData1().getName())
        elif action.getType() == 'look':
            if action.getPlayerRef().getName() == owner.getName():
                pass
            else:
                action.getPlayerRef().writePlain('\r\n'+owner.getName()+' is here.')
        elif action.getType() == 'vision':
            owner.writeWithPrompt(action.getString())
            return
        else:
            pass