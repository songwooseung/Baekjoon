import sys
input = sys.stdin.readline

arr = [0] * 10001 # 배열 0부터 시작

N = int(input())

for i in range(N):
    arr[int(input())] += 1

for i in range(len(arr)):
    for _ in range(arr[i]):
        print(i)
