import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()

# 기술을 reverse 해야 2,3 조건을 사용할 수 있음. 
tech = list(map(int,input().split()))
tech.reverse()

# for range 써서 append i + 1 이런 방식으로도 쓸 수 있음.
index = 1
for i in tech : 
    if i == 1 : 
        dq.appendleft(index)
    elif i == 2 :
        dq.insert(1,index)
    elif i == 3 :
        dq.append(index)
    
    index += 1 


print(*dq)

