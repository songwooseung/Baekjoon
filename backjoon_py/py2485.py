# 백준 문제 2485번: 가로수
import sys
from math import gcd

input = sys.stdin.readline

N = int(input())

# 가로수 줄 한줄씩 입력하고 오름차순으로 정렬된 채로 배열에 집어넣기
arr = sorted([int(input()) for i in range(0,N)])
arr2 = []

# 각 가로수의 차를 새로운 배열에 집어넣기
for i in range(1,N):
    arr2.append(arr[i]-arr[i-1])


g = arr2[0]
for j in range(0,len(arr2)-1):
    g = gcd(g,arr2[j+1])

result = 0 

# 사이에 지을 수 있는 그루 수 구하기. 
# 여기서 arr2와 g를 나누고 -1을 한 이유는 g를 2번 곱했을 때 arr2[n] 값이랑 동일하면 그 사이의 값이 아니라 그루의 위치가 겹치게 되므로 몫을 -1해주는 것이다.
for each in arr2:
    result += (each // g) - 1 
print(result)