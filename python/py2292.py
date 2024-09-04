# 2292
# 2023-10-06 11:49:01
N = int(input())
cnt = 1 # 지나가는 방의 갯수
x = 1
while(True):
    if N <= x :
        break
    
    x += cnt*6
    cnt += 1
print("%d" %cnt) 
    