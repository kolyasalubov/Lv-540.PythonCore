#Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один 
#використовуючи цикл while, а інший з використанням циклу for).

#for number in range (1,100,2):
#    print ("Непарне число: ",number)

#for number in range (1,100):
 #   if number %2==0:
 #       print ("Парне число: ",number)

#number = 1
#while number < 100:
 #   if number %2 == 0:
#     print ("Парне число: ",number)
#  number +=1

# number = 1
# while number < 100:
#     if number %2 != 0:
#         print ("Непарне число: ",number)
#     number +=1


# #Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.
# number = int (input ("Please enter the number: "))
# if number % 2 == 0:
#     print (f"{number} is even")
# else: print (f"{number} is odd")

#Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

# for number in range (1, 100):
#     if number % 2 ==0:
#         continue
#     print (f"{number} is odd")

# number = 1
# while number < 100:
#     if number % 2 ==0:
#         number +=1
#         continue
#     print (f"{number} is odd")
#     number +=1

#  Перевірити чи список містить непарні числа.(Підказка: використати оператор break)
# numbers = (input ("Please enter numbers:"))
# list_of_numbers = list(numbers.replace(" ", ""))
# list_of_numbers_int = [int(number) for number in list_of_numbers]

# for number in list_of_numbers_int:
#     if number %2 != 0:
#         print ("This list has odd number") 
#         break
# else:
#     print ("This list has all even numbers") 

#   4.  Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# # (Підказка: використати вбудовану функцію float ()).

list_int = [4, 5, 6]

for i in range(len(list_int)):
   list_int [i] = float (list_int [i])
print (list_int)

list_int = [float(list_int [i]) for i in range(len(list_int))]
print (list_int)