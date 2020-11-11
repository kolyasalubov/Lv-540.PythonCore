

import func
import math
# from math import pi

user_questions=int(input("Choose: 1: rectangle, 2: triangle, 3: circle "))

if user_questions == 1:
    a = int(input("Enter the lengh of rectangle: "))
    b = int(input("Enter the width of rectangle: "))
    print("The square of rectangle is: ", func.rectangle(a,b))

if user_questions == 2:
    a = int(input("Enter the base of triangle: "))
    h = int(input("Enter the heigh of triangle: "))
    print("The square of triangle is: ", func.triangle(a,h))    

if user_questions == 3:
    a = math.pi
    r = int(input("Enter the radius of circle: "))
    print("The square of circle is: ", func.circle(a,r))    
