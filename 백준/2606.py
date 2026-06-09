from collections import deque

node = int(input())
edge = int(input())

graph = [[] for i in range(node+1)]

visited = [0] * (node+1)

for i in range(edge):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = 1
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
            
# bfs(1)
dfs(1)
print(sum(visited)-1)