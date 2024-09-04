# 1453
n = int(input())
arr = [0] * n
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(n-1):
    if(arr[i] == arr[i+1]):
        cnt += 1
print(cnt)   