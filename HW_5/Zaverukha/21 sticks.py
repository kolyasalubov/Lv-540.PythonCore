def make_move(sticks):
    for i in range(1,4):
        if (sticks-i) % 4 == 0:
            return i