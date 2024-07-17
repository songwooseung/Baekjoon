import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

S = 0 
min_num = 0

for i in range(M, N+1):
    if i == 1 :
        continue

    # 제곱근 으로 소수 판별하는 방법
    for j in range(2,int(i**0.5)+1):
        if i%j == 0 :
            break

    # for문이 정상적으로 종료 됐다면 실행
    else :
        if S == 0 :
            min_num = i
        S += i

if S > 0 : 
    print(S)
    print(min_num)
else :
    print(-1)