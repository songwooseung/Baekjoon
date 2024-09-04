# 15649 N, M(1) 수열과 달리 이번 문제는 모든 수열이 오름차순으로 고르게 정렬이 되어야 한다.

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr =  []

# 오름차순으로 나타내기 위한 start 매개변수 선언 
def seq(start):

    if len(arr) == M :
        return print(' '.join(map(str,arr)))


    
    for i in range(start,N+1):
        # 1 1, 2 2와 같이 중복된 값은 배제한다.
        if i not in arr:
            arr.append(i)
            seq(i+1)
            arr.pop()


seq(1)