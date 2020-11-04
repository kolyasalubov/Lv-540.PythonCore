def average(n):
    a=0
    for i in range(n):
        i=int(input("Enter element: "))
        a+=i
    print("Average number is: ", str(a/n))
number=int(input("Enter number: "))
average(number)
