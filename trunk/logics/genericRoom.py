def process(action, owner):
    if action.getType() == 'look':
        c = action.getPlayerRef()
        c.writePlain('['+owner.getName()+']\r\n')
        c.writePlain(owner.getDesc()+'\r\n')
        for eachExit in owner.getPortals().values():
            c.writePlain('['+eachExit.getName()+'] ')
            
        c.writeWithPrompt("")