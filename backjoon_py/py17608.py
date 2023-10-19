# 17608번 문제:

# 1번 째 방법
'''
import sys # sys.stdin.readline() 사용하기 위함 -> input()보다 빠르고 시간 초과를 피할 수 있다. 
N = int(input())
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = int(sys.stdin.readline())
cnt = 1
max = arr[N-1] # max = arr[-1]
for i in reversed(range(N)):
    if arr[i] > max:
        cnt += 1 
        max = arr[i] # max 값 갱신, max보다 큰 막대기가 보이면 max 갱신
        # 계속 max 값을 갱신하면서 max보다 큰 막대기가 보이면 cnt += 1 해줘야 함.
print(cnt)  
'''
# 2번 째 방법
import sys
N = int(input())
arr = [0] * N
cnt = 1
for i in range(N) :
    arr[i] = int(sys.stdin.readline())

max = arr[-1]
for i in reversed(range(N)):
    if arr[i] > max : 
        cnt += 1
        max = arr[i]
print(cnt)
