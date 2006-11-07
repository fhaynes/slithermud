### basicRoomLogic.py
### (c)2004 Fletcher Haynes, All Rights Reserved
### 12-15-04

import MudWorld
import MudAction
import MudProtocol
def Execute(owner, action):
    if action.actionType == 'look':
        new_action = MudAction.MudAction()
        new_action.actionType = 'cansee'
        res = owner.doAction(new_action)
        if res == 1:
            return
        action.playerRef.writePlain('\r\n['+str(owner.id_num)+']\r\n')
        action.playerRef.writePlain('<cyan>['+owner.name+']<r><blue><r>\r\n')
        action.playerRef.writePlain(MudProtocol.wrapText(owner.desc)+'\r\n')
    else:
        pass