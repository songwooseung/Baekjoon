import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = min(N,M)
arr = []
cnt = 0

for i in range(N):
    arr.append(list(input().strip()))


for i in range(N) :
    for j in range(M):
        # j는 cnt를 구할 때 직접적으로 계산하지는 않는다. 
        for k in range(S) :
            # and는 개별적으로 값을 비교하는 것이기 때문에 == 보다 정확도가 떨어진다.
            if((i+k < N and j+k < M) 
               and arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]):    
                # j 값을 기준으로 얼마나 차이가 나는지 찾는 게 k
                # 크기가 같은 정사각형이니 제곱을 해준다.
                cnt = max(cnt,(k+1)**2) 
                
print(cnt)

