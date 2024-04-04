import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(N):
    stack = []
    word = input().strip()
    for j in word :
        if stack and stack[-1] == j :
            stack.pop(-1)
        else :
            stack.append(j)
    if not stack :
        cnt += 1
print(cnt)