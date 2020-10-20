#task1
i=0
for i in range (0,99,2):
  print ("\tВсі парні числа менші 100:", i)

#task2
i = int(input("Enter  your number: "))
if i % 2 == 0:
  print("Your number", i, " is even ")
else:
  print("Your number", i, "is odd") 

#task3
l = [2, 4, 8, 0, 67, 78, 101]
for i in l:
  if not i % 2 == 0:
    contains_odd = True
    break
print('List contains odd', i)


