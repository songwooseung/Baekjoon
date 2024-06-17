import sys
input = sys.stdin.readline


N, M = map(int,input().split())

arr1 = set() # add update remove
arr2 = set()  

for i in range(N):
    arr1.add(input().strip())
for i in range(M):
    arr2.add(input().strip())


arr3 = sorted(list(arr1 & arr2))

# 결과
print(len(arr3))
for i in arr3 :
    print(i)