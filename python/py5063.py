import sys
input = sys.stdin.readline

N = int(input())

for i in range(0,N):
    r,e,c = map(int,input().split())
    if r == (e-c) : 
        print(f"does not matter")
    elif r < (e-c) : 
        print(f"advertise")
    else :
        print("do not advertise")
