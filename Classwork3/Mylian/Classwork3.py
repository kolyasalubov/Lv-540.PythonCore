#Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

def find_avarage():
    l_1=[]
    n=int(input("Заповніть список стількома елементами: "))
    for value in range(n):
        l_1.append(int(input("Введіть елементи: ")))
    print("Список: ", l_1)  

    arithmetic_mean=sum(l_1)/len(l_1)
    print("Середнє арифметичне: ", arithmetic_mean)
find_avarage() 

#Написати функцію, яка знаходить найбільше число з двох чисел, а також в функції використати рядки документації DocStrings.

def largest_number(a,b):
    """Функція знаходить більше число з двох"""
    if a>b:
        print("Число",a,"є більше аніж", b)
    else:
        print("Число",b,"є більше аніж", a)   

print(largest_number.__doc__)   
largest_number(10,6)   

#Написати програму, яка обчислює площу прямокутника, трикутника та кола 

def rectangle(lengh,width):
    return lengh*width
square=rectangle(5,4)   
print("Площа прямокутника =", square)

    #2 варіант
    # def rectangle():
    #     lengh=int(input("Введіть довжину сторони:"))
    #     width=int(input("Введіть ширину сторони:"))
    #     square=lengh*width
    #     print("Площа прямокутника =", square)
    # rectangle()

def triangle(base,heigth):
    return 1/2 * base*heigth
square=triangle(5,4)   
print("Площа трикутника =", square)   

def circle():
    PI=3.14
    radius=float(input("Введіть радіус:"))
    square=PI*radius**2  
    print("Площа кола =", square) 
circle() 

#Написати функцію, яка обчислює кількість символів, які входять в задану стрічку

def count_symbols():
    symbols=input("Введіть символи: ")
    count_of_symbols=len(symbols)
    print("Кількість символів, які входять в задану стрічку:", count_of_symbols)
count_symbols()    