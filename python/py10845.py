import sys
input = sys.stdin.readline

def push(x):
    queue.append(x)

def pop():
    if queue : 
        return queue.pop(0)
    else :
        return -1 

def size():
    return len(queue)

def empty():
    return 0 if len(queue) else 1

def front():
    return queue[0] if len(queue) else -1 

def back():
    return queue[-1] if len(queue) else -1

N = int(input())
queue = []

for _ in range(N):
    cmd = input().split()

    if(cmd[0] == 'push'):
        push(cmd[1])
    elif(cmd[0] == 'pop'):
        print(pop())
    elif(cmd[0] == 'size'):
        print(size())
    elif(cmd[0] == 'empty'):
        print(empty())
    elif(cmd[0] == 'front'):
        print(front())
    elif(cmd[0] == 'back'):
        print(back())
    else :
        print("다시 입력하세요 ")

        