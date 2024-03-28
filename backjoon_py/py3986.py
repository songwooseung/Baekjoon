import sys
input = sys.stdin.readline

N = int(input())
cnt = 0 

for i in range(N):
    stack = []
    arr = list(input().strip())
    for j in arr :
        if len(stack) == 0:
            stack.append(j)
        elif stack[-1] == j :
            stack.pop(-1)
        else : 
            stack.append(j)
    if len(stack) == 0:
        cnt+=1
print(cnt)