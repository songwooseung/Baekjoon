import sys 
input = sys.stdin.readline

N = int(input())

for i in range(N):
    L = list(map(str,input().split())) 
    L.reverse()
    print(f'Case #{i+1}:', ' '.join(L))