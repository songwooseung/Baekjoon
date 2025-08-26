import sys
from collections import deque

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    
    while queue :    
        n = queue.popleft()
        print(n, end=" ")

        for i in graph[n] :
            if visited_bfs[i] == False :
                queue.append(i)
                visited_bfs[i] = True
    
def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")

    for i in graph[v] :
        if visited_dfs[i] == False :
            dfs(i)
            
    


N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)] # 0번 노드 비워두기 위해 N+1

for i in range(M):
    x, y = map(int,input().split())
    graph[x].append(y) 
    graph[y].append(x)

for i in range(1,N+1): # 0번째 노드는 비어있으니까
    graph[i].sort()    

visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)

dfs(V)
print()
bfs(V)

