w = []
numbers = int(input('Enter your number:'))
for i in range(numbers):
    w.append(int(input('Enter your number:')))
print(min(w))
print(max(w))

# task 1
number_1 = int(input("Enter your number: "))
if number_1 % 2 == 0:
    print("Your number is even")
else: 
    print("Your number is odd")

#task 2 
for i in range(0, 100, 2):
    print(i)
first = 0
while first < 100:
    print(first)
    first += 2

# task 3
for value in range(1, 100, 2):
    print(value)

for var in range(100):
    if var%2 ==0:
        continue
    else:
        print(var)

task 4
list_1 = []
list_numbers = int(input("Enter numbers: "))
for e in range(list_numbers):
    list_1.append(int(input("Enter your numbers: ")))
for s in range (0, list_numbers):
    if list_1[0]%2 != 0:
        print("List have even numbers")
        break
    else:
        list_1[0] += 1
