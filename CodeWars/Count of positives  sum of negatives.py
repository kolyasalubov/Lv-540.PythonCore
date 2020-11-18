def count_positives_sum_negatives(arr):
    if arr==[]: 
        return []
    
    positive=0
    negative=0
    
    for x in arr:
        if x > 0:
            positive+=1
        else: 
            negative+=x
    return[positive, negative] 
