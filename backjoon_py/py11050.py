import sys

def fact(N):
    if N <= 1 :
        return 1 # 반복문이 정상적으로 종료
    else :
        return N * fact(N-1)


n, k = map(int,sys.stdin.readline().split())

print(fact(n) // (fact(n-k) * fact(k)))

