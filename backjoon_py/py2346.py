import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())

# enumerate는 index와 값을 튜플 형식으로 같이 저장된다. (0,3),(1,2) ......
dq = deque(enumerate(map(int,input().split())))
result = []

while dq :
    index, number = dq.popleft()
    result.append(index+1) # 1 부터 저장

    if number > 0 :
        dq.rotate(-(number-1))

    elif number < 0 :
        dq.rotate(-number)


print(*result)