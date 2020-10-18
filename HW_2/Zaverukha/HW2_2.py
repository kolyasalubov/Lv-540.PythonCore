 
number = 3852
f1 = number%10
f2 = number%100//10
f3 = number%1000//100
f4 = number%10000//1000
print(f1, f2, f3, f4)
print("Multiply = ", f1*f2*f3*f4)

number = str(number)
print("Reversed", number[::-1])
