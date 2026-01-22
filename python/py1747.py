# 백준 1747 소수 & 팰린드롬

import sys
input = sys.stdin.readline

def is_pd(n):
   n = str(n)
   return n == n[::-1]

'''
사용자가 입력을 1,000,000 내로 한다고 해도 결과는 N 이상의 소수면서 팰린드롬인 최소 수를 구하는거니까

사용자가 23, 35같은 작은 숫자가 아니라 1,000,000 을 딱 입력받는다고 하면 이 숫자 이상의 값의 소수를 미리 체크해놔야하니

제한을 2,000,000으로 두고 넉넉하게 둠 
'''
num = 2000000 
k = int(input())

is_prime = [True] * num
is_prime[0] = is_prime[1] = False # 이거 [False]로 넣으면 새 리스트로 들어가짐.
# primes=[] # 소수 체크용

for i in range(2,num):
  if is_prime[i]:
    # primes.append(i) 
    for j in range(2*i, num, i):
        is_prime[j] = False
        

for i in range(k,num):
    if is_pd(i) and is_prime[i] :
        print(i)
        break



