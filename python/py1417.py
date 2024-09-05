import sys
input = sys.stdin.readline

candidate = []
cnt = 0

N = int(input())
dasom = int(input())
for _ in range(N-1):
    candidate.append(int(input()))

if candidate :
    while max(candidate) >= dasom : 
        cnt += 1 
        # max(candidate) 값이 있는 index 찾아서 -1 해주기
        candidate[candidate.index(max(candidate))] -= 1
        dasom += 1
    
print(cnt)


