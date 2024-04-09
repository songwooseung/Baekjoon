import sys 
N = int(sys.stdin.readline())

cnt = 0
num = 666

while True :
    if '666' in str(num):
        cnt += 1 
    
    if cnt == N :
        break
    
    num += 1 
print(num)
