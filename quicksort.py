import numpy as np

def _partition(array, first, last):
    pivot_val = array[first]
    i = first
    for j in range(i, last):
        if array[j] < pivot_val:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[first], array[i] = array[i], array[first]
    return i

def _quicksort(array, first, last):
    if last - first <= 1:
        return
    pivot = _partition(array, first, last)
    _quicksort(array, first, pivot)
    _quicksort(array, pivot+1, last)
    
def quicksort(array):
    _quicksort(array, 0, len(array))

n = 7
a = range(n)
np.random.shuffle(a)
print(a)
quicksort(a)
print(a)

