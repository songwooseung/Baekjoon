# 정수의 모든 경우의 수를 순서대로 뽑아주는 함수
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
