def distance(p1, p2):
    return -1 if len(p1)!=len(p2) or len(p1) == 0 else sum((p1[n]-p2[n])**2 for n in range(len(p1)))**0.5