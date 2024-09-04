# pop(0) 시 맨 앞의 정수를 삭제 후 다시 정렬해줘야 하므로 시간이 많이 걸린다.
# 따라서 입력값의 범위가 클 때에는 무조건 deque를 사용해주자.

import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

def push(X):
    return queue.append(X)

def pop():
    if queue : 
        return queue.popleft()
    else :
        return -1

def size():
    return len(queue)

def empty():
    if queue : 
        return 0
    else :
        return 1

def front():
    if queue :
        return queue[0]
    else :
        return -1

def back():
    if queue :
        return queue[-1]
    else :
        return -1


N = int(input())

for i in range(N):
    x = input().split() # 공백 마다 문자 나누기
    
    if x[0] == 'push' : 
        push(x[1])
    elif x[0] == 'pop' :
        print(pop())
    elif x[0] == 'size' :
        print(size())
    elif x[0] == 'empty' :
        print(empty())
    elif x[0] == 'front' :
        print(front())
    elif x[0] == 'back' :
        print(back())
