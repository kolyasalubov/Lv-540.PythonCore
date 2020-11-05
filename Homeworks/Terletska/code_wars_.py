def distance(x1, y1, x2, y2):
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    return round(d,2)
print(distance(int(input()),int(input()),int(input()),int(input())))
