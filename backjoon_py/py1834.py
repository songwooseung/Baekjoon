import sys

input = sys.stdin.readline
N = int(input())
sum = 0

# 검토식을 활용해서 시간초과 막는 방법

for i in range(1, N):
    sum += N * i + i # N = 3 -> 3 * 1 + 1 , 3 * 2 + 2 
    
print(sum)