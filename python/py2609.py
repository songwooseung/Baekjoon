def gcd(a,b):
    r = 0
    while b != 0 :
        r = a % b 
        a = b 
        b = r
    return a

def lcm(a, b):
    return (a*b) // gcd(n1,n2)

n1,n2 = map(int,input().split())

print(gcd(n1,n2))
print(lcm(n1,n2))