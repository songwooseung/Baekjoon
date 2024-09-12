import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0 : 
        c = a%b
        a = b
        b = c 
    return a

def rcd(a,b):
    return (a*b) // gcd(a,b)

N = int(input())


for _ in range(N):
    x, y = map(int,input().split())
    print(rcd(x,y),gcd(x,y))



