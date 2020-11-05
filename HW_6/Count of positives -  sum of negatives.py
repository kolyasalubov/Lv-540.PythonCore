# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


def count_positives_sum_negatives(arr):
    # if arr is None or len(arr) == 0:
    if (arr == None or arr == []):
        return []
    else:
        count_positive_numbers = 0
        sum_of_negative_numbers = 0
        for element in arr:
            if element  > 0:
                count_positive_numbers +=1
            else:
                sum_of_negative_numbers += element
        return [count_positive_numbers, sum_of_negative_numbers]

print (count_positives_sum_negatives(None))