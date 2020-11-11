import random

random_number=random.randint(1,100)
# print(random_number)
user_number=int(input("Quess the number: "))
while True:
    if user_number==random_number:
        print("Wow! You have quessed the number;)")
        break
    
    elif user_number < random_number:
        user_number=int(input("Enter bigger number: "))

    elif user_number > random_number:
        user_number=int(input("Enter smaller number: "))