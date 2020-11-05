import random
def make_move(sticks):
    if sticks % 4 != 0:
        return sticks % 4
    else:
        return random.randint(1, 3)
