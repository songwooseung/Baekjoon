N, M = map(int,input().split())
cnt = 0 

S = set()

for _ in range(N):
    S.add(input())

for _ in range(M):
    word = input()

    if word in S : 
        cnt += 1

print(cnt)