def makeMove(sticks):
    return sticks % 4 or 1
print(makeMove(int(input())))
