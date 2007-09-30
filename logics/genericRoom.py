def process(action, owner):
    if action.getType() == 'look':
        c = action.getPlayerRef()
        c.writeWithPrompt(owner.getDesc())