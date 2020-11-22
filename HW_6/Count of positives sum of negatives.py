def count_positives_sum_negatives(arr):
    if arr ==[]:
        return []
    pos = 0
    neg = 0
    for number in arr:
        if number > 0:
            pos +=1
        else:
            neg +=number
    return [pos, neg]