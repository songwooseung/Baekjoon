import sys
N = int(sys.stdin.readline())
for i in range(N-1):
    for j in range(i):   
        print(' ',end="")
    for k in range(2*N-1-(i*2)):
        print('*',end="")
    print(' ')

for i in range(N):
    for j in range(N-1-i):
        print(' ',end="")
    for k in range(0,1+(i*2)):
        print('*', end = "")
    print(' ')