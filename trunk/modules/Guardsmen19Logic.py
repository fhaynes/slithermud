import MudWorld
def Execute(owner, action):
    if action.actionType == 'enterroom' and owner.name != action.playerRef.name:
        MudWorld.world.handleInput(owner, 'say Another [refugee], eh?')
    elif action.actionType == 'say' and owner.name != action.playerRef.name:
        if 'refugee' in action.string.lower():
            MudWorld.world.handleInput(owner, "say We've been getting a lot of you lot since the [invasion].\
 You best go join one of the Guilds in the city. The Council don't like bums, so make yourself useful!")
        elif 'invasion' in action.string.lower():
            MudWorld.world.handleInput(owner, "say We heard that the demons have taken over most of the upper lands\
 so we got all you survivors comin' down here. We're not too happy about it, either!")
        else:
            pass
    else:
        pass