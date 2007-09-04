import MudDatabase
import MudAction


def Execute(owner, action):
    if action.actionType == 'say':
        new_action = MudAction.MudAction()
        new_action.actionType = 'canhear'
        res = owner.doAction(new_action)
        if res == 1:
            return
        else:
            if owner.name.lower() == action.playerRef.name.lower():
                pass
            else:
                owner.writeWithPrompt(action.playerRef.name+' says, "'+action.string+'"')
    elif action.actionType == 'leaveroom':
        new_action.MudAction.MudAction()
        new_action.actionType = 'cansee'
        res = owner.doAction(new_action)
        if res == 1:
            return
        else:
            if owner.name == action.playerRef.name:
                pass
            else:
                owner.writeWithPrompt(action.playerRef.name+' leaves '+action.data1.lower())
    elif action.actionType == 'look':
        if action.playerRef.name == owner.name:
            pass
        else:
            action.playerRef.writePlain('\r\n['+str(owner.id_num)+'] <red>'+owner.name+' is here.<r>')
    elif action.actionType == 'vision':
        # Need to check if blind and such
        owner.writeWithPrompt(action.string)
    elif action.actionType == 'getitem':
        #Do this with a vision event, maybe?
        owner.writeWithPrompt(action.playerRef.name+ ' gets '+action.data1.name)
    elif action.actionType == 'dropitem':
        owner.writeWithPrompt(action.playerRef.name+ ' drops '+action.data1.name)
    elif action.actionType == 'lookat':
        new_action = MudAction.MudAction()
        new_action.actionType = 'isvisible'
        new_action.playerRef = action.playerRef
        res = owner.doAction(new_action)
        if res == 1:
            return
        else:
            action.playerRef.writeWithPrompt(owner.desc)
    elif action.actionType == 'tick':
        MudDatabase.db.saveCharToDisk(owner)
        
    else:
        pass