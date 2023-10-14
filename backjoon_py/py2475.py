# 2475
# 2023-10-15 01:47:18
arr = list(map(int,input().split()))
sum = 0
for i in range(len(arr)):
    arr[i] = arr[i]**2
    sum += arr[i]
sum %= 10
print(sum)