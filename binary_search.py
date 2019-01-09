import numpy as np


def _binary_search(a, l, r):
    if l >= r:
        if a[l] == k:
            return l
        else:
            return None
    m = (l + r)//2
    if a[m] < k:
        return _binary_search(a, m+1, r)
    elif a[m] > k:
        return _binary_search(a, l, m-1)
    else:
        return m
    
def binary_search(a, k):
    if len(a) == 0:
        return None
    l = 0
    r = len(a) - 1
    return _binary_search(a, l, r)


a = sorted(np.random.randint(-5, 5, 10).tolist())
k = np.random.randint(-5, 5)
print(a)
print(k)
print(binary_search(a, k))

i, j = 0, len(a)-1
while(True):
    if(j < i):
        print(None)
        break
    m = (i + j)//2
    if k < a[m]:
        j = m-1
    elif k > a[m]:
        i = m+1
    else:
        print(m)
        break
    

