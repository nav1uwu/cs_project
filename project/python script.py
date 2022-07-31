import eel
eel.init('web')
state = ' '

##def abcd(name):
##    name = str(name)
##    output = name
##    print( output)
@eel.expose
def sendstate(state_param):
    global state
    state = state_param
    print (state)
    eel.change_state(state)
    





eel.start('main.html')
