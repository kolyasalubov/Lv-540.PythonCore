four_digit_number = input('4 digit number please : ')

mult = 1 

for digit in str(four_digit_number):
    mult *= int(digit)

print('mult of digits : ',mult)
print('Reversed number : ', four_digit_number[::-1])
print('Sorted number',''.join(sorted(str(four_digit_number))))

