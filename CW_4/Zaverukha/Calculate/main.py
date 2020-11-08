import calc
user_question = int(input("Enter:1 - +, 2 - -, 3 - *, 4 - /"))

if user_question == 1:
    t1 = int(input("Enter fist number - "))
    t2 = int(input("Enter second number - "))
    add = calc.addition(t1, t2)
    print(add)
if user_question == 2:
    t1 = int(input("Enter fist number - "))
    t2 = int(input("Enter second number - "))
    subs = calc.subtraction(t1, t2)
    print(subs)
if user_question == 3:
    t1 = int(input("Enter fist number - "))
    t2 = int(input("Enter second number - "))
    multi = calc.multiplication(t1, t2)
    print(multi)
if user_question == 4:
    t1 = int(input("Enter fist number - "))
    t2 = int(input("Enter second number - "))
    divi = calc.division(t1, t2)
    print(divi)