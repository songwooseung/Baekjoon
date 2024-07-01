# two pointer 

N = int(input())

left = 1
right = 1
cnt = 1
res = 1

while(right != N):
    if res < N :
        right += 1
        res += right

    elif res > N:  
        res -= left
        left += 1 
    
    elif res == N :
        cnt += 1 
        right += 1 
        res += right
        
print(cnt)

