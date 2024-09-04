# 7568
import sys
input = sys.stdin.readline
N = int(input())
h = []
for i in range(N):
    h.append(list(map(int,input().split()))) # append 시 이차원 배열 가능

for i in h : # 배열 전체가 한 번에 들어가는 게 아니라, 인덱스 하나 씩 뽑아서 넣음
    k = 1 # k 
    for j in h :
        if i[0] < j[0] and i[1] < j[1]: # 처음 인덱스 부터 끝까지 비교해서 자신보다 몸무게, 키가 크면 등수 + 1 하기  
            k += 1
    print(k,end=' ')
    