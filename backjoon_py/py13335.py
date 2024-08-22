import sys
from collections import deque
input = sys.stdin.readline


n, w, l = map(int,input().split())
truck =  deque(map(int, input().split()))

# 다리 크기 재기 
q = deque(0 for i in range(w)) 
# 걸린 시간
time = 0 

while q :
    time += 1 
    q.popleft() # truck이 비어 있을 경우 q.popleft을 반복하여 while 탈출 

    if truck : 
        if sum(q) +  truck[0] <= l :
            q.append(truck.popleft())
        else : 
            q.append(0)

print(time)
