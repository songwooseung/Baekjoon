# 9095
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0, 1, 2, 4] # i가 1일땐 1, i가 2일땐 1+1, 2, i가 3일 때는 1+1+1, 1+2, 2+1, 3
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    print(dp[n])
    