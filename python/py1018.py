import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []
cnt = []

for _ in range(N): # 줄마다 초기화
    arr.append(input().strip())


for A in range(N-7): # 8*8
    for B in range(M-7): # 8*8
        # 홀수, 짝수 index를 비교
        # 정상적인 패턴이 나타난다면 정상 인덱스에 저장, 어긋난 부분은 비정상 인덱스에 저장
        index1 = 0 # 패턴이 B로 시작할때 정상이 되는 index
        index2 = 0 # 패턴이 W로 시작할때 정상이 되는 index
        
        for i in range(A,A+8): # A < A+8 일 때까지 반복
            for j in range(B,B+8):
                if (i+j) % 2 == 0 :
                    if arr[i][j] != 'W' :
                        index1 += 1 
                    else :
                        index2 += 1 
                else :
                    if arr[i][j] != 'B' :
                        index1 += 1
                    else :
                        index2 += 1
        cnt.append(min(index1,index2))

print(min(cnt))
