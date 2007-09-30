def process(action, owner):
    if action.getType() == 'say':
        owner.writeWithPrompt(action.getPlayerRef().getName()+ ' says, "'+action.getString()+'"')
        