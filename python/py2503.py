# 복습하기
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
number = list(permutations(range(1,10),3))

# N번 반복
for _ in range(N):
    base, s, b = map(int,input().split())

    # temp는 매 반복마다 초기화해줌
    temp = []

    for cheak in number :
        cnt_s, cnt_b = 0,0
        for i, value in enumerate(str(base)):
            if int(value) == cheak[i] :
                cnt_s += 1
            elif int(value) != cheak[i] and int(value) in cheak :
                cnt_b += 1  
        
        if s == cnt_s and b == cnt_b :
            temp.append(cheak)
            
    # 조건에 해당하는 temp로 값을 교체해서 비교 대상을 줄임
    number = temp 


print(len(temp))
