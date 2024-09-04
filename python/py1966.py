import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    cnt = 0 
    while q :
        if q[0] < max(q):
            q.append(q.pop(0))
        else :
            if m == 0 : break
            q.pop(0) 
            cnt += 1 
        
        # m = m - 1 if m > 0 else len(q) - 1
        if m > 0 : m -= 1
        else : m = len(q)-1 # M이 0이고 목표값이 아니라면 배열의 마지막 원소길이로 
    print(cnt+1)