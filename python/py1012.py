import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False 
    
    if graph[x][y] == 1 :
        graph[x][y] = 0

        # 해당 방향을 기준으로 연결되는 부분 모두 탐색
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        # 결국 배추가 심어진 땅을 하나라도 발견했다면 True임
        return True
    
    # 발견 못할시
    return False 
    

T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0] * M for _ in range(N)]
    yb = deque()
    res = 0

    for _ in range(K):
        x,y = map(int,input().split())
        yb.append(((y,x)))
        graph[y][x] = 1
        
    while yb :
        nx, ny = yb.popleft()
        if dfs(nx,ny) == True : 
            res += 1

    print(res)
              







# M,N,K = map(int,input().split())

# graph = [[0] * M for i in range(N)]

# print(graph)

# for i in range(K):
#     x, y = map(int,input().split())

#     graph[y][x] = 1

# print(graph)

