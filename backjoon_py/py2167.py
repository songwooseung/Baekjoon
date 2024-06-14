import sys
input = sys.stdin.readline

N, M = map(int,input().split())
li = []

for i in range(N):
    li.append(list(map(int,input().split())))

K = int(input())

for _ in range(K):
    i,j,x,y = map(int,input().split())
    sum = 0

    for a in range(i-1,x):
        for b in range(j-1,y): 
            sum += li[a][b]
    
    print(sum)