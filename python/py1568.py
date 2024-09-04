import sys 

N = int(sys.stdin.readline())
K = 1 
cnt = 0

while N > 0 :
    if K > N :
        K = 1 
    
    N -= K
    K += 1
    cnt += 1

print(cnt)
