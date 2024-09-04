import sys
N, M = map(int, sys.stdin.readline().split())

cnt = 1
num = 0

if N == 0 :
    cnt = 0
else :
    arr = list(map(int,sys.stdin.readline().split()))
    for i in arr :
        if (num+i) <= M :
            num += i
        else :
            num = i # M을 초과했으므로 다음 상자로 넘어 갔음을 의미 (이 값은 다음 반복문에서 사용)
            cnt += 1
        
print(cnt)