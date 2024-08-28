import sys
from collections import deque

deq = deque()

def front_input(X):
    return deq.appendleft(X)

def back_input(X):
    return deq.append(X)

def front_pop():
    if deq :
        return deq.popleft()
    else :
        return -1

def back_pop():
    if deq :
        return deq.pop()
    else :
        return -1

def size():
    return len(deq)

def empty():
    if deq : 
        return 0
    else :
        return 1

def front_print():
    if deq : 
        return deq[0]
    else :
        return -1

def back_print():
    if deq : 
        return deq[-1]
    else :
        return -1
    

N = int(sys.stdin.readline())

for _ in range(N):
    x = sys.stdin.readline().split()

    if x[0] == '1' :
        front_input(int(x[1]))
    elif x[0] == '2' :
        back_input(int(x[1]))
    elif x[0] == '3' :
        print(front_pop())
    elif x[0] == '4' :
        print(back_pop())
    elif x[0] == '5' :
        print(size())
    elif x[0] == '6' :
        print(empty())
    elif x[0] == '7' :
        print(front_print())
    elif x[0] == '8' :
        print(back_print())
    

