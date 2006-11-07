
import MudAction
def Execute(owner, action):
    if action.actionType == 'look':
        new_action = MudAction.MudAction()
        new_action.actionType = 'cansee'
        res = action.playerRef.doAction(new_action)
        if res == 1:
            return
        action.playerRef.writePlain('\r\n<green>['+str(owner.id_num)+'] '+owner.name+' is here.<r>')

    else:
        pass