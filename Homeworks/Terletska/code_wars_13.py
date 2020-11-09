def count_positives_sum_negatives(arr):
    arr2=[]
    sumn=0
    sump=0
    if len(arr)==0:
        return []
    for i in arr:
        if i>0:
            sump+=1
        else:
            sumn+=i
    arr2.append(sump)
    arr2.append(sumn)
    return arr2
