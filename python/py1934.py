import sys
input = sys.stdin.readline

# 최대공약수 : 유클리드 호제법을 이용한 최대공약수 구하기
def gcd(a,b):    
    while b != 0 :
        r = a % b
        a = b
        b = r 
    return a

# 최소공배수 : A*B를 최대공약수로 나눠서 최소공배수 구하기 
def lcm(a,b):
    return (a*b) // gcd(a,b)
    
T = int(input())

for _ in range(T):
    A, B = map(int,input().split())
    print(lcm(A,B))


        
         