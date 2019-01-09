from collections import deque
graph = {0:[1],
         1:[2,3],
         2:[1,3,4,5],
         3:[1,2,6,7,8],
         4:[2],
         5:[2,9],
         6:[3,9],
         7:[3],
         8:[8],
         9:[6,5]}

#DFS iterative
visited = [False]*len(graph)
stack = deque([0])
while stack:
    v = stack.pop()
    if visited[v] == False:
        visited[v] = True
        print(v)
        for adj in graph[v]:
            if visited[adj] == False:
                stack.append(adj)
                
#BFS
print
visited = [False]*len(graph)
queue = deque([0])
while queue:
    v = queue.popleft()
    if visited[v] == False:
        visited[v] = True
        print(v)
        for adj in graph[v]:
            if visited[adj] == False:
                queue.append(adj)
 
#DFS recursive
print
def dfs(graph, v, visited):
    if visited[v] == True:
        return
    print(v)
    visited[v] = True
    for adj in graph[v]:
        dfs(graph, adj, visited)

visited = [False]*len(graph)
dfs(graph, 0, visited)
        
    