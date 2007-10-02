def process(action, owner):
    if action.getType() == 'say':
        owner.writeWithPrompt(action.getPlayerRef().getName()+ ' says, "'+action.getString()+'"')
    elif action.getType() == 'enterroom':
        owner.writeWithPrompt(action.getPlayerRef().getName()+ ' enters via '+ action.getData1().getName())
    elif action.getType() == 'leaveroom':
        owner.writeWithPrompt(action.getPlayerRef().getName()+ ' exits via '+action.getData1().getName())
    else:
        pass