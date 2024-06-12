import sys
N = int(sys.stdin.readline())

# 정수를 문자열로 바꾸고, 각 자리수가 4 or 7인지 확인한다.
def check(num):
    num = str(num)
    for i in num :
        if i != '4' and i != '7' :
            return False
    return True 
    
# 가장 큰 수를 찾는 것이니까, N부터 시작한다. (N은 4이상)
for i in range(N, 0, -1):
    if check(i):
        print(i)
        break 


