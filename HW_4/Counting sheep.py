# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array 
# (true means present). c

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    number_of_sheeps= 0
    for i in sheep:
        if i ==True:
            number_of_sheeps += 1
    return number_of_sheeps 

