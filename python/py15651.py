import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = []
def bt() :
    
    if len(arr) == M :
        return print(' '.join(map(str,arr)))

    for i in range(1,N+1):
        arr.append(i)
        bt()
        arr.pop()

bt()