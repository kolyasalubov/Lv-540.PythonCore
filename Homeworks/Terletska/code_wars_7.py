def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
    pass
arr=[True,False,True,True]
print(count_sheeps(arr))
