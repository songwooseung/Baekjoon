# N 이상 M 이하의 소수를 모두 출력하는 프로그램

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

for i in range(N, M+1):
    if i == 1: # 1은 소수가 아님 // N이 1부터 시작할 수 있음
        continue

    # 소수 판별은 제곱근을 활용하여 구할 수 있다. -> 모든 수를 비교하며 찾는거보다 제곱근을 이용해 찾는 것이 더 효율적
    # 제곱근은 i^1/2 이므로 i**0.5이다. 
    # Ex) 12의 제곱근은 2*루트3이므로 약 3.4정도 된다.

    for j in range(2,int((i**0.5)+1)):
        if i%j == 0 :
            break   

    # for 루프의 else문은 for 루프가 정상적으로 실행됐을 때 실행하는 조건문이다.
    # 만약 for문이 break문에 의해 탈출할 시 else문은 실행되지 않는다. 
    else :
        print(i)


    
        
    


