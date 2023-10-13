# 10810
# 2023-10-14 00:14:03
n, m = map(int,input().split())
arr = [0] * n # 0을 n번 집어넣어서 초기화 시키기 

for x in range(m):
    i, j, k = map(int,input().split())
    for y in range(i,j+1):
        arr[y-1] = k
        

for x in arr:
    print(x,end=" ")
