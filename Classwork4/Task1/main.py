import calc

user_questions=int(input("Choose: 1: +, 2: -, 3: *, 4: / "))

if user_questions == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(calc.addition(a,b))

if user_questions == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(calc.subtraction(a,b))    

if user_questions == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(calc.multiplication(a,b)) 

if user_questions == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(calc.division(a,b))         