# 백트래킹 문제
# permutations 함수를 사용해 간단하게 수열을 생성할 수 있다.

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = []

def seq():

    if len(S) == M :
        return print(' '.join(map(str,S)))


    for i in range(1,N+1):
        if i not in S : 
            # ex : 4 2 입력 시 1 - 2 - 3 - 4 을 기준으로 수열 생성
            S.append(i)
            seq()
            S.pop()

seq()