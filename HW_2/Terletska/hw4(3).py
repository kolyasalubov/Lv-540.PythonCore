def triangle(a,h):
    s=0.5*a*h
    print(s)

def rectangle(a,b):
    s=a*b
    print(s)

def circle(r):
    s=3.14*(r**2)
    print(s)

k=input("Enter figure: ")
if k==triangle:
    triangle(int(input("Enter a:")), int(input("Enter h:")))
elif k==rectangle:
    rectangle(int(input("Enter a:")), int(input("Enter b:")))
elif k==circle:
    circle(int(input("Enter r:")))



