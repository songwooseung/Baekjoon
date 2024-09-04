# 행렬에 대해서 더 자세하게 공부하도록

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = []
B = []

for i in range(N):
    A.append(list(map(int,input().split())))
    # A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int,input().split())

for i in range(M):
    B.append(list(map(int,input().split())))
    # B = [list(map(int, input().split())) for _ in range(M)]

C = [[0] * K for _ in range(N)] 

for i in range(N):
    for j in range(K):
        result = 0
        for k in range(M):
            result += A[i][k] * B[k][j]
        C[i][j] = result

for i in C :
    print(*i)

'''
for i in C:
    for j in i :
        print(j, end=" ")
    print()
'''