# 2506
# 2023-10-11 07:08:44
N = int(input())
arr = list(map(int,input().split()))
sum = 0 
cnt = 0
for i in range(0,N):
    if arr[i] == 1 :
        cnt += 1
        sum += cnt
    else :
        cnt = 0
print(sum)