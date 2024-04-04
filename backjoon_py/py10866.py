from collections import deque
import sys
input = sys.stdin.readline

def push_front(x):
    d.appendleft(x)
def push_back(x):
    d.append(x)

def pop_front():
    if d :
        return d.popleft()
    else :
        return -1
def pop_back():
    if d :
        return d.pop()
    else :
        return -1

def size():
    return len(d)

def empty():
    return 0 if d else 1 

def front():
    return d[0] if d else -1

def back():
    return d[-1] if d else -1

N = int(input())
d = deque()

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push_front' :
        push_front(cmd[1])
    elif cmd[0] == 'push_back' :
        push_back(cmd[1])
    elif cmd[0] == 'pop_front' :
        print(pop_front())
    elif cmd[0] == 'pop_back' :
        print(pop_back())
    elif cmd[0] == 'size' :
        print(size())
    elif cmd[0] == 'empty' :
        print(empty())
    elif cmd[0] == 'front' :
        print(front())
    elif cmd[0] == 'back' :
        print(back())
    else :
        print("다시 입력하세요")
    