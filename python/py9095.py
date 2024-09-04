# 9095
import sys
input = sys.stdin.readline
'''
# 첫 번째 방법
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0, 1, 2, 4] # i가 1일땐 1, i가 2일땐 1+1, 2, i가 3일 때는 1+1+1, 1+2, 2+1, 3
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    print(dp[n])
'''   
'''
# 두 번째 방법
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (n+1) 
    
    for i in range(1,n+1): # 0은 양수가 아니니 제외
        if n == 1:
            dp[i] = 1
        if n == 2:
            dp[i] = 2 
        if n == 3:
            dp[i] = 3
        else :
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
'''
# 세 번째 방법 
t = int(input())

dp = [0] * 11 # n은 11보다 작다고 했으니 0~10까지 총 11개 방 생성
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(0, t):
    n = int(input())
    print(dp[n])
    
    
    
    