import sys
N = int(sys.stdin.readline())

# 피보나치 수 문제를 수행하듯 점화식을 구해 문제를 수행한다.
# 점화식 : (n > 1), dp[n] = dp[n - 2] + dp[n - 1]
if N == 1 :
    print(1)
else : 
    dp = [0] * N 
    dp[0] = 1
    dp[1] = 1 # N == 2 일때 10이니까 1로 초기화 

    for i in range(2,N):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N-1])