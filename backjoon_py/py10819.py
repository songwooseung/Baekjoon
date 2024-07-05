# 1. itertools 함수로 푼 방법
# from itertools import permutations
import sys 
from itertools import permutations 

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

# 튜플 형태로 저장
arr2 = list(permutations(arr, N)) 

result = 0

for li in arr2 :
    total = 0 
    for i in range(N-1):
        total += abs(li[i]-li[i+1])
    
    result = max(result, total)

print(result)

# 2. 백트래킹으로 구현한 방법 

# n = int(input())
# in_list = list(map(int ,input().split()))
# visited = [False]*n
# answer = 0
# def sol(li):
#   global answer
#   if len(li) == n:
#     total = 0
#     for i in range(n-1):
#       total += abs(li[i]- li[i+1])
#     answer = max(answer, total)
#     return

#   for i in range(n):
#     if not visited[i]:
#       visited[i] = True
#       li.append(in_list[i])
#       sol(li)
#       visited[i] = False
#       li.pop()

# sol([])
# print(answer)