def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive = 0
    negative = 0
    for x in arr:
        if x > 0:
            positive += 1
        if x < 0:
            negative += x
    return [positive, negative]
