A, B = map(int,input().split())

def gcd(A,B):
    if B == 0 :
        return A
    else : return gcd(B,A%B)

def lcm(A,B):
    return int((A*B)/gcd(A,B))

r = lcm(A,B)
print(r)