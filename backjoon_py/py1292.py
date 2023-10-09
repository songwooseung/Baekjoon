# 1292
# 2023-10-10 08:12:38
A, B = map(int, input().split())
arr = []
sum = 0

for i in range(1, B+1): # 1부터 B까지 반복
    arr += [i] * i # arr에 i번째 수를 i번 반복해서 넣는다

for i in range(A-1, B): # 배열은 0부터 시작하니까 A-1 < B까지 반복한다.
    sum += arr[i]

print(sum)