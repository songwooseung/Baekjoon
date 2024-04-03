# 이거 꼭 다시 풀고 제대로 이해하기
import sys
input = sys.stdin.readline

def dfs(weight,cnt):
    global ans

    if weight < 500 : 
        return 
    
    if cnt >= N : 
        ans += 1 
        return

    for i in range(N):
        if tree[i] == 0:
            tree[i] = 1
            dfs(weight+arr[i]-K,cnt+1)
            tree[i] = 0

N, K = map(int,input().split())
arr = list(map(int,input().split())) 
ans = 0
tree = [0] * N

dfs(500,0)

print(ans)