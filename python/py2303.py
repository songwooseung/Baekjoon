# 브루트포스 알고리즘 : 조합 가능한 모든 문자 or 정수를 하나씩 대입해보는 방식
import sys
input = sys.stdin.readline
N = int(input())

score = []

for _ in range(N):
    arr = list(map(int,input().split()))  
    max_num = 0
    # i == 3 이면 k가 5이므로 다시 for문을 반복 그 다음 반복에서 j가 5가 되므로 반복 종료
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                max_num = max(max_num,(arr[i]+arr[j]+arr[k]) % 10)
    score.append(max_num)
    
# score가 같을 때 번호가 가장 큰 사람의 번호를 출력해야하니까 index는 뒤에서부터 시작
for i in range(N-1,-1,-1):
    if score[i] == max(score):
        print(i+1)
        break 

'''
i=0, j=1, k=2 일 때, (arr[0]+arr[1]+arr[2]) % 10 = (7+5+5) % 10 = 7
i=0, j=1, k=3 일 때, (arr[0]+arr[1]+arr[3]) % 10 = (7+5+4) % 10 = 6
i=0, j=1, k=4 일 때, (arr[0]+arr[1]+arr[4]) % 10 = (7+5+9) % 10 = 1
i=0, j=2, k=3 일 때, (arr[0]+arr[2]+arr[3]) % 10 = (7+5+4) % 10 = 6
i=0, j=2, k=4 일 때, (arr[0]+arr[2]+arr[4]) % 10 = (7+5+9) % 10 = 1
i=0, j=3, k=4 일 때, (arr[0]+arr[3]+arr[4]) % 10 = (7+4+9) % 10 = 0
i=1, j=2, k=3 일 때, (arr[1]+arr[2]+arr[3]) % 10 = (5+5+4) % 10 = 4
i=1, j=2, k=4 일 때, (arr[1]+arr[2]+arr[4]) % 10 = (5+5+9) % 10 = 9
i=1, j=3, k=4 일 때, (arr[1]+arr[3]+arr[4]) % 10 = (5+4+9) % 10 = 8
i=2, j=3, k=4 일 때, (arr[2]+arr[3]+arr[4]) % 10 = (5+4+9) % 10 = 8
'''
        

