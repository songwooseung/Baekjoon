# 한 줄로 서기 : 1138
import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int,input().split()))
res = [0] * N


for i in range(N):
    cnt = 0
    for j in range(N):
        if res[j] == 0:
            if cnt == line[i]:
                res[j] = i+1
                break # 줄 위치 삽입 시 for j문 탈출
            cnt += 1 # 빈공간있을 시 if문 안돌아가면 cnt만 증가시키고 다시 반복

print(*res)





























# N = int(input())
# line = list(map(int, input().split()))
# result = [0] * N

# for i in range(N):
#     count = 0
#     for j in range(N):
#         if result[j] == 0:
#             if count == line[i]:
#                 result[j] = i + 1
#                 break
#             count += 1

# print(' '.join(map(str, result)))