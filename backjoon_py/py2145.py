# 2145
while(True):
    n = int(input())
    if n == 0:
        break
    
    while(n >= 10): # n이 673일 때
        tmp = 0 # n 이 10보다 클 때 매번 새로운 값을 받아주기 위한 tmp 선언
        while(n > 0): # tmp에 3+7+6 = 16 돌아가고 빠져나옴
            tmp += n % 10
            n //= 10
        n = tmp # tmp의 값인 16을 n에 다시 넣어주고 n >= 10인지 확인해주고 다시 while(n>0) 반복문 돌아감
    print(n)
            