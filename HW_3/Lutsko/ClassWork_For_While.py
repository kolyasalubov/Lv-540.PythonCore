############################# 1 even/odd number
a = int(input('Please enter number a: '))
if a%2 == 0: 
    print(a, 'is an even number')
else: 
    print(a, 'is an odd number')
############################# even number <100
start = 0
finish = 100
while start < finish:
    print(start)
    start +=2
else: 
    print('The end')
############################# 2 even number <100
for j in range(0,100,2):
    print(j)
else:
    print('The end')
#############################
for j in range(1,100,2):
    print(j)
else:
    print('The end')
############################# 3 odd number <100
for j in range(100):
    if not j%2 == 0:
          continue
    print(j)
else:
    print('The end')
############################# 
print(list(range(1,100,2)))

############################# 4 
a = list(range(0,100,3))
print(a)
for j in a:
    if not j%2 == 0:
         print("There are odd numbers")
         break
else:
    print('There are only even numbers')

############################# 5 change type
a = list(range(0,100))
print(a)
for index, j in enumerate(a):
       a[index] = float(j)

print(a)
print(type(a))

