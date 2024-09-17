from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
TF = [[False for i in range(N)] for i in range(N)]
res = 0

for i in range(M):
    idx1, idx2 = map(int,input().split())
    TF[idx1-1][idx2-1] = True 
    TF[idx2-1][idx1-1] = True # 조합은 순서가 없으니까 반대도 True로 바꿔줌

for i in combinations(range(N),3) : # 조합 하나씩 집어넣음 i에
    if TF[i[0]][i[1]] or TF[i[1]][i[2]] or TF[i[0]][i[2]] :
        continue
    res += 1

print(res)

# for i in range(N):
#     for j in range(i+1,N):
#         for k in range(j+1,N):
#             if not TF[i][j] and not TF[i][k] and not TF[k][j] : # 어차피 반대 방향으로 True을 다 해놔서 6개의 조건중에 고르면 됨
#                 res += 1

