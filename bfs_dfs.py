g = {0:[1,2,3],\
     1:[4,5],\
     2:[6,7],\
     3:[8,9],\
     4:[],\
     5:[],\
     6:[],\
     7:[],\
     8:[],\
     9:[]}

def search(g, v=0, style='BFS'):
    deque = [v]
    while deque:
        v = deque.pop(0)
        print("visiting: ", v)
        if style == 'BFS':
            deque = deque + g[v]
        else:
            deque = g[v] + deque
search(g, 0, 'BFS')
print(' ')
search(g, 0, 'DFS')

    
