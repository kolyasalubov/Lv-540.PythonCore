#number = int(input('Please enter number:'))

number = int(2145)

# multiplication
d1 = number % 10
d2 = number % 100 // 10
d3 = number // 100 % 10
d4 = number // 1000
print(d1, d2, d3, d4)
print('multiplication=', d1*d2*d3*d4)

# reverted number
str = str(number)
print('reverted number = ', int(str[::-1]))

# sorted numbers
ascending = "".join(sorted(str))
print('ascending = ', int(ascending))
descending = ascending[::-1]
print('descending = ', int(descending))