def list_animals(animals):
    list = ''
    for item in range(len(animals)):
        list += str(item + 1) + '. ' + animals[item] + '\n'
    return list