import sys
input = sys.stdin.readline

N = int(input())
G, S = 0, 0 
arr = []

for i in range(N):
    sleep = input().strip()
    arr.append(list(sleep))

for i in range(N):
    t = 0 
    for j in range(N):
        if arr[i][j] == '.':
            t += 1 
            if t == 2 :
                G += 1
        else :
            t = 0

for i in range(N):
    t = 0 
    for j in range(N):    
        if arr[j][i] == '.':
            t += 1 
            if t == 2 :
                S += 1 
        else :
            t = 0


print(G,S)
