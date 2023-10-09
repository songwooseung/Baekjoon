N = int(input())
M = 1
'''
(1) C스타일로 푼 문제
while(M <= N):
    num = M
    sum = M # 초기화
    while(num > 0): #각 자리수 뽑아서 sum에 더하기 (기존에 M이 들어가있는 상태)
        sum += num % 10
        num = num // 10
    if (sum == N): #sum이 n값과 같으면 M출력 후 종료
        print(M)
        N = 0
        break
    M += 1 #못 찾으면 M++ 후 다시 while 돌기

if(N != 0) : 
    print("0") #sum과 N이 같을 때 N = 0으로 만들었으므로 만약 while문을 다돌아도 값을 못찾으면 0출력
''' 
while M <= N :
    SUM = M + sum(map(int,str(M))) # 이렇게 사용하면 각 자릿수의 합을 구할 수 있다. (M을 string으로 하나하나 뽑아서) 
    if(SUM == N):
        print(M) 
        N = 0
        break
    M +=1

if N != 0:
    print("0")
# 또는 else : print("0") 사용이 가능하다 -> while문이 거짓이 되면서 바깥에 있는 else문이 실행된다
# 그렇기 때문에 while문 안의 if문이 참이 되어 break문이 실행되면 else문이 실행되지 않는다.
    

    
    
    
     
    
    
    