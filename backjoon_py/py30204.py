# 30204번: 병영외 급식
# 2023-10-08 12:10:30
N, X = map(int,input().split())
a = list(map(int,input().split()))
sum = 0
for i in range(N):
    sum += a[i]

if sum % X == 0:
    print("1")
else:
    print("0")