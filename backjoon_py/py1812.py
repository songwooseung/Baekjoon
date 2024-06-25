import sys 

input = sys.stdin.readline

N = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

if A-B : 
    print(len(A-B))
    for i in sorted(A-B) : # 정답이 되려면 정렬을 해야하더라. (set은 순서 상관 X)
        print(i,end=" ")
else :
    print(0)
