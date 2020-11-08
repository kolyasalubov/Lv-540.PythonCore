import func
choose_figure = int(input("Choose figure(1-triangle, 2-circle, 3-rectangle)"))
if choose_figure == 1:
    a_side = int(input("Enter a-side:\n"))
    height_side = int(input("Enter b-side:\n"))
    print(func.rectangle(a_side, height_side))
if choose_figure == 2:
    radius = int(input("Enter radius of circle:\n"))
    print(func.circle(radius))
if choose_figure == 3:
    a_side = int(input("Enter a-side:\n"))
    b_side = int(input("Enter a-side:\n"))
    print(func.rectangle(a_side, b_side))