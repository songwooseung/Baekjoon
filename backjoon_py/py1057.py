import sys 
input = sys.stdin.readline

N, KIM, LIM = map(int,input().split())
cnt = 0 

# 1은 1-0 이므로 올라갈 때 계속 고정임. 
# 이런 알고리즘은 잘 숙지해두기 
while(KIM != LIM) :
    KIM -= KIM // 2
    LIM -= LIM // 2 
    cnt += 1  

print(cnt)