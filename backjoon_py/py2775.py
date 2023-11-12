# 2775 
import sys
input = sys.stdin.readline

t = int(input()) # test case 

for _ in range (t):
    k = int(input()) # 층 
    n = int(input()) # 호
    
    floor = [i for i in range(1,n+1)] # 0층의 i호에는 i명이 살고있다.
    
    for i in range(k): 
        for j in range(1, n): # 1호 제외 / 1호의 아래층에는 1호만 있으므로 1 고정이기 때문
            floor[j] += floor[j-1] # j 값 누적하여 1호부터 n호까지 합구하기 
    print(floor[n-1]) # 값의 합이 저장되어 있는 n호 출력
    
        