import math
def triangle(a_side, height_side):
    area_triangle = 0.5*a_side*height_side
    return f"Area of triangle is {area_triangle}"
def circle(radius):
    area_circle = math.pi*math.pow(radius, 2)*0.5
    return f"Area of circle is {area_circle}"
def rectangle(a_side, b_side):
    area_rectangle = a_side*b_side
    return f"Area of rectangle is {area_rectangle}"