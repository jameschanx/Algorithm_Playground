import numpy as np

class Heap:
    def __init__(self, array, style='min'):
        self.style = style
        self.heap = [0] + array
        self.size = len(array)
        i = self.size
        for i in range(self.size//2, 0, -1):
            self._percDown(i)

    
    def _swap_child(self, i):
        compare = [(self.heap[i], i)]
        if i * 2 <= self.size:
            compare.append((self.heap[i*2], i*2))
        if i * 2 + 1 <= self.size:
            compare.append((self.heap[i*2+1], i*2+1))
        if self.style == 'min':
            return min(compare)[1]
        if self.style == 'max':
            return max(compare)[1]
    
    def _percDown(self, i):
        while i <= self.size:
            c = self._swap_child(i)
            if i == c:
                break
            self.heap[i], self.heap[c] = self.heap[c], self.heap[i]
            i = c
    
    def remove(self):
        if self.size == 0:
            return
        ret_val = self.heap[1]
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self._percDown(1)
        return ret_val
    
    def _percUp(self, i):
        while i != 0:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]    
                i = i//2
            else:
                break

    def insert(self, val):
        pass

    def disp(self):
        if self.size == 0:
            return
        i = 1
        print(self.size * '  ', [self.heap[i]])
        parents = [i]
        while parents:
            children = []
            display = []
            for j in parents:

                sub = []
                if j*2 <= self.size:
                    children.append(j*2)
                    sub.append(self.heap[j*2])
                if j*2+1 <= self.size:
                    children.append(j*2+1)
                    sub.append(self.heap[j*2+1])
                display.append(sub)
            if j >= self.size:
                break
            indent = (self.size - j) * '  '
            print(indent, display)
            parents = children
            
a = list(np.random.randint(0,100,size=10))

h = Heap(a, 'max')
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()
print(h.remove())
h.disp()

