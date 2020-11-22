def count_sheeps(sheep):
    array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
    count_sheeps = 0
    for x in array1:
        if x == True:
            count_sheeps += 1
    return count_sheeps