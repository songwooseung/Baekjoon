# 함수를 이용한 풀이
import sys
input = sys.stdin.readline

def nmg(n): 
    cnt = 0
    while(n > 0):
        if n % 5 == 0 :
            cnt += n // 5
            break
        else :
            n -= 2 
            cnt += 1 

    if n < 0 :
        print("-1")
    else :
        print(cnt)
if __name__ == '__main__': # python의 main함수
    money = int(input())
    nmg(money)
    




# 간단한 풀이
'''
n = int(input())
cnt = 0
while(n > 0):
    if n % 5 == 0 :
        cnt += n // 5
        break
    else :
        n -= 2 
        cnt += 1 
    
if n < 0 :
    print("-1")
else :
    print(cnt)
'''