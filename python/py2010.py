import sys
input = sys.stdin.readline
N = int(input())
res = 0
for i in range(0,N):
    num = int(input())
    if (i != N-1) : 
        res += (num-1)
    else :
        res += num
print(res)