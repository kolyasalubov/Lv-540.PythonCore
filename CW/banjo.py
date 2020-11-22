name = list(str(input("What is your name ? ")))
if name[0] == 'R' or name[0] == 'r':
    print(''.join(name), " plays banjo")
else:
    print(name, " does not play banjo")