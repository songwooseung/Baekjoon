import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
left, right = 0, 1

while (left <= right and right <= N):

    total = sum(A[left:right])

    if(total < M):
        right += 1
    elif(total > M):
        left += 1
    
    else :
        cnt += 1
        right += 1 # 여기서 오른쪽으로 한칸 안땡기면 cnt 무한 증가 
print(cnt)