import numpy as np


def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[i+j] = left[i]
            i += 1
        else:
            array[i+j] = right[j]
            j += 1
    if i < len(left):
        array[j+i:] = left[i:]
        i = len(left)
    
    if j < len(right):
        array[j+i:] = right[j:]
    return array
        
n = 10
a = range(n)
np.random.shuffle(a)
print(a)
mergesort(a)
print(a)
