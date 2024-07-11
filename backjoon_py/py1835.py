# 다시 풀어보기 

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()


for i in range(N , 0, -1): # 4 ~ 1 까지 반복 
    dq.appendleft(i)

    if len(dq) > 1 :
        for j in range(i):
            dq.appendleft(dq.pop()) # 힌트 가장 앞에 있는 것을 뒤로 i번 옮긴다의 역
            
print(*dq) 


'''
힌트
1. 2 1 4 3에서 2를 가장 뒤로 옮긴다. (1 4 3 2)
2. 1을 책상 위에 옮겨놓는다. (4 3 2)
3. 4 3 2 에서 4, 3을 뒤로 옮긴다. (2 4 3)
4. 2를 책상 위로 옮겨놓는다. (4 3)
5. 4 3 에서 가장 앞에 있는 것을 뒤로 3번 옮긴    다. (3 4)
6. 3을 책상 위로 옮겨놓는다. (4)
7. 4를 책상 위로 옮겨놓는다. (완료)

'''