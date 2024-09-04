import sys
N = int(sys.stdin.readline())
cnt = 0
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
# 팩토리얼 확인 
# print(fact(N))

cheak = fact(N)

while True :
    if cheak % 10 == 0 :
        cnt += 1
        cheak //= 10  
    else :
        break
print(cnt)