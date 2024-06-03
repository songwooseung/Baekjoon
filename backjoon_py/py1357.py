import sys
input = sys.stdin.readline

def Rev(x) :
    res = 0
    while (x > 0) :
        res += x % 10
        x //= 10
        
        if x > 0 : 
            res *= 10 

    return res

n, m = map(int, input().split())
print(Rev(Rev(n) + Rev(m)))
