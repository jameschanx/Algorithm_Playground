import numpy as np

def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        
        mergesort(left_array)
        mergesort(right_array)
        
        i, j = 0, 0
        while(i < len(left_array) and j < len(right_array)):
            if left_array[i] < right_array[j]:
                array[i+j] = left_array[i]
                i += 1
            else:
                array[i+j] = right_array[j]
                j += 1
        
        if(i < len(left_array)):
            array[i+j:] = left_array[i:]
            
        if(j < len(right_array)):
            array[i+j:] = right_array[j:]
            

n = 10
a = range(n)
np.random.shuffle(a)
print(a)
mergesort(a)
print(a)
