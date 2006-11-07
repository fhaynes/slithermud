import MudAction
def Execute(owner, action):
    if action.actionType == 'enterportal':
        pass
    elif action.actionType == 'look':
        new_action = MudAction.MudAction()
        new_action.actionType = 'cansee'
        res = owner.doAction(new_action)
        if res == 1:
            return
        action.playerRef.writePlain('<bright><red>['+owner.name+'] <r>')
    else:
        pass