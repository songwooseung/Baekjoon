# 1145
n = list(map(int,input().split()))
min = min(n) # 굳이 이렇게 시작안해도 됨. num = 1해서 1씩 증가시켜도됨, 효율성 떄문에 이렇게 함. -> 최소한 나눌 수 있는 수부터 시작하기 위함 . 
# num = 1 
while True : 
    cnt = 0  # 3개 못찾을 시 cnt를 0으로 초기화
    
    for i in n :
        if min % i == 0 : # num % i == 0 
            cnt += 1
    if cnt > 2 : # cnt == 3은 안된다. for문이 끝까지 돌아 갔을 때 cnt가 3보다 클 수도 있기 떄문이다.
        break
    
    min += 1 # num += 1 
    
print(min) # num    