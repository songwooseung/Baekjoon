def gcd(a,b) :
    while b != 0 :
        r = b
        b = a % b
        a = r 
    return a

x, y = map(int,input().split(':'))
d = gcd(x,y)
print(f'{x // d}:{y // d}')

