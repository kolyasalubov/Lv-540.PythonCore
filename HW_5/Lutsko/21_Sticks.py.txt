import random
def makeMove(sticks):
    if sticks % 4 != 0:
        return sticks % 4
    else:
        return random.randint(1, 3)