import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
q = deque([i for i in range(1,N+1)])
cnt = 0 

for i in range(M):
    while True : 
        if q[0] == target[i] :
            q.popleft()
            break
        else :
            if q.index(target[i]) <= len(q) // 2 : # 큐 절반 길이보다 작거나 같으면 왼쪽으로 이동하자 (최소 루트)
                q.rotate(-1) # 왼쪽으로 한 칸씩 이동 -> q.append(q.popleft())
                cnt += 1 
            else :
                q.rotate(1) # 오른쪽으로 한 칸씩 이동 -> q.appendleft(q.pop())
                cnt += 1 
                
print(cnt)



