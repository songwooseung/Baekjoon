import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input())
cnt = 1

while True :
    x = int(input())

    if x == -1 :
        break

    if cnt > N :
        pass
    elif x > 0 :
        queue.append(x)
        cnt += 1

    if queue and x == 0: 
        queue.popleft()
        cnt -= 1 
    
if queue :
    print(' '.join(map(str,queue)))
else :
    print('empty')
