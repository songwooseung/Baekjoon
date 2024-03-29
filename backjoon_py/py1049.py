# 그리디 알고리즘 : 최소 값을 구하는 데에 사용되는 근사적인 방법
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
cost = 0
cnt = N 

# 각 브랜드의 pack, piece를 입력 받을 때마다, 최소 pack과 최소 piece를 새로운 변수에 저장한다. 
for i in range(M):
    pack, piece = map(int,input().split())
    if i == 0: # 처음에 들어오는 pack, piece는 이후 비교를 위해 모두 min 변수에 집어넣는다 
        min_pack = pack
        min_piece = piece 
    else :
        min_pack = min(min_pack, pack)
        min_piece = min(min_piece, piece)

# cnt가 6 이상일 때랑 6 미만일 때를 이용해 최소 cost를 변수에 저장
while True :
    if cnt >= 6  :
        if min_pack < min_piece*6 :
            cost += min_pack
            cnt -= 6
        else : 
            cost += min_piece
            cnt -= 1
    
    else :
        if cnt * min_piece > min_pack: 
            cost += min_pack
            cnt -= 6 
        else : 
            cost += min_piece
            cnt -= 1

    if cnt <= 0 : break

print(cost)
