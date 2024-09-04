import sys
input = sys.stdin.readline

def push(x):
    stack.append(x)

def pop():
    if stack :
        return stack.pop()
    else :
        return -1

def size():
    return len(stack)

def empty():
    return 1 if len(stack) == 0 else 0 # 1 이상일 경우 참이니까 1, 0일 경우 거짓이니 0

def top() :
    return stack[-1] if len(stack) > 0 else -1

N = int(input())
stack = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        print(pop())
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        print(empty())
    elif cmd[0] == 'top':
        print(top())
    else :
        print("잘 못 입력하셨습니다")
        break

