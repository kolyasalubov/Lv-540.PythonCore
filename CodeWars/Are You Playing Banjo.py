def areYouPlayingBanjo(name):

    if name[0] == 'R':
        return name + ' plays banjo'
    elif name[0] == 'r':   
        return name + ' plays banjo' 
    else: 
        return name + ' does not play banjo'   

##################################################
def areYouPlayingBanjo():

    str=input("Name ")
    if str[0] == 'R':
        print("You are playing banjo!")
    elif str[0] == 'r':   
        print("You are playing banjo!") 
    else: 
        print("You are not playing banjo!")    
areYouPlayingBanjo() 