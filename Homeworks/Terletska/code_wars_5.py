def areYouPlayingBanjo(name):
    if name[0]=='r' or name[0]=='R':
        return name + ' plays banjo'
    return name + ' does not play banjo'
print(areYouPlayingBanjo(input()))
