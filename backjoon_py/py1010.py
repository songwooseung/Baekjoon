def fact(n) :
    num = 1
    if n == 1 :
        return n # 어차피 1부터 곱하니까 필요가 없긴 함. 
    for i in range(1, n+1):
        num *= i
    return num 

t = int(input())

for _ in range(0,t) : 
    N, M = map(int,input().split())
    link = fact(M) // (fact(M-N)*fact(N))
    print(link)
    