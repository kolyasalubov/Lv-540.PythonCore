# Задано чотирицифрове натуральне число. 
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

number = int(input ("Вкажіть чотирицифрове натуральне число: "))
first_digit = number // 1000
second_digit = (number%1000) // 100
third_digit = (number%100) // 10
fourth_digit = (number%10)
print ("Добуток цифр цього числа: ",first_digit* second_digit* third_digit * fourth_digit)

string_number = str(number)
print ("number in reverse order:", string_number[::-1])
all_digits = ([first_digit, second_digit, third_digit, fourth_digit])
all_digits.sort()
str_all_digits = [str(digit) for digit in all_digits]
joined_str_all_digits = ''.join(str_all_digits)
print("sorted digites:", joined_str_all_digits)