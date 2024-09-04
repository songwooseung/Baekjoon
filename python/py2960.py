import sys
input = sys.stdin.readline

N, K = map(int,input().split())

num = [i for i in range(2,N+1)]
dnum = []

# print(num) 
for i in range(2, N+1):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0 :
            break

    # for문 정상 실행 시 실행
    else : 
        # print('-----------------------------') -> 각 소수마다 삭제 과정 보이기
        pnum = i
        while pnum <= N :
            if pnum in num :
                dnum.append(pnum)
                num.remove(pnum) 
                # print(num)
            pnum += i 
                
print(dnum[K-1])


    



