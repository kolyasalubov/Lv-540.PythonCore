number = input("Enter a four-digit natural number: ")
a = int(number)

the_product_of_the_digits_of_this_number = (a//1000)*(a%10)*((a//100)%10)*((a%100)//10)
print("The product of numbers: ", the_product_of_the_digits_of_this_number)

print ("The number is sorted in reverse order: ",number[::-1])

print("The number is sorted in ascending order: ",(sorted(number)))