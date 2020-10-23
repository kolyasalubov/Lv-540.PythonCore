#1
i=int(input("Number: "))
if i % 2==0:
    print("Число парне")
else:    
    print("Число непарне")

#2 парні числа <100(while)
    n=0
while n<100:
    n=n+1
    if n % 2==0:
         print(n)

#2 парні числа <100(for)
n=0
for n in range(101):
    if n%2==0:
        print(n)

#3 непарні числа <100
n=0
while n<100:
    n=n+1
    if n % 2==1:
         print(n)

#3 непарні числа <100
for i in range(100):
     if i % 2 == 1:
        print(i)

#4
c_list = [10, 12, 3, 8, 1, 14, 4,]
for i in c_list:
  if i % 2 == 1:
    break
print("Знайдено непарне число: ", i)

#5
c_list=[2,3,5,6,8,9]
for a in c_list:
    c_list=float(a)
    print("З плаваючою крапкою: ", c_list)
        

        