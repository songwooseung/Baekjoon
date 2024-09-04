# 11653
N = int(input())
i = 2
while N > 1 :
    if N % i == 0 : 
        print(i)
        N //= i
        i = 2
    else :
        i += 1 