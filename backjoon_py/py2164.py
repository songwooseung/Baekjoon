# deque (스택, 큐, 리스트 간단하게 구현 가능) 
# https://dongdongfather.tistory.com/72
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

deque = deque([i+1 for i in range(0,N)])
#print(deque)

while len(deque) > 1 :
    deque.popleft()
    tmp = deque.popleft()
    deque.append(tmp)
print(deque[0])