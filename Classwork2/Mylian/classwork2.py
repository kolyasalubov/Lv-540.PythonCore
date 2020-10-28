########Створити список цілих чисел які вводяться з терміналу, знайти min,max
l_1=[]
n=int(input("Заповніть список: "))
for value in range(n):
    l_1.append(int(input("Наступні елементи: ")))

print("Список: ", l_1)   

largest=max(l_1)
smallest=min(l_1)
print("Максимальний ел: ", largest)
print("Мінімальний ел: ", smallest)

######## В інтервалі від 1 до 10 визначити числа
for i in range(1,11):
    if i%2 ==0:
        print("Парні числа: ", i)
for i in range(1,11):
    if i%3 ==0 and i%2 ==1:
         print("Непарні, які діляться на 3: ", i)   
for i in range(1,11):
    if i%3>=1<=2 and i%2 ==1:
         print("Числа не діляться на 2 і на 3: ", i)

####### Перевірити логін юзінг (while)
login=input("Enter your login: ")
while login != 'First':
    print("Your login is incorrect! Try again")  
    break
else:
    print("Congrats! You logged out successfully!")      