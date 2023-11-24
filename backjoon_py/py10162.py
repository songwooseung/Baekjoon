# 10162
import sys
input = sys.stdin.readline
N = int(input())

# 첫 번째 방법
arr = [0,0,0]
if N % 10 != 0 : 
    print("-1")
    exit()
if N // 300 :
    arr[0] += N // 300
    N %= 300 
if N // 60 :
    arr[1] += N // 60
    N %= 60
if N // 10 : 
    arr[2] += N // 10

for i in arr :
    print(i, end=" ")

'''
# 두 번째 방법
# 부분 100점
if N % 10 != 0 :
    print("-1")
else : 
    for i in [300,60,10] :
        print(N//i, end=" ")
        N %= i
'''