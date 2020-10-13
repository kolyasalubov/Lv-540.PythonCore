a = int(input('Add first numer \n'))
operation = input('Choose operation : \n')
b = int(input('Add second numer \n'))


if operation == '+':
    print(a+b)
elif operation =='-' :
    print(a-b)
elif operation =='*':
    print(a*b)
elif operation =='.':
    print(a/b)
elif operation =='**':
    print(a**b)