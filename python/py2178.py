from collections import deque

def bfs():
    queue = deque([(0,0)])

    while queue :
        x,y = queue.popleft()

        for i in range(4): # 4방향으로 한 방향씩 위치 측정
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 초과시 탈출 / 다른 방향으로 테스트
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M :
                continue 
            
            # 벽을 마주할 시 탈출
            if graph[nx][ny] == 0 :
                continue
            
            # 현재 위치에서 이동+방문하지 않은 길 마주할 시 현재 위치(지금까지 거쳐온 수) + 1로 체크해주고 큐에 해당 위치 삽입
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    # 큐에 최종적으로 비게 되면 (N-1,M-1) 좌표의 거리 출력
    return print(graph[N-1][M-1])

# 상,하,좌,우
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

N,M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().strip())))

bfs()

'''
tc1
4 6
101111
101010
101011
111011

tc2
4 6
110110
110110
111111
111101
'''