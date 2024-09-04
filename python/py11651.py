import sys

N = int(sys.stdin.readline())
area = [] 

for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    area.append((x,y)) # (y,x) 형식으로 집어넣어서 sorted방식으로 다른 변수에 집어 넣어도 됨. 

area.sort(key=lambda x : (x[1],x[0])) # 1차 기준 x[1] , 2차 기준 x[0]
# 내림차순 : area.sort(key=lambda x: (-x[0], -x[1]))

for i in range(N):
    print(area[i][0],area[i][1])