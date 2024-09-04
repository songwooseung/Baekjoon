import sys
input = sys.stdin.readline

N = int(input())
cnt = 0 

for _ in range(N):
    word = input().strip()
    previous_word = ''
    check = set()
    tr = True 

    for char in word : 
        if char != previous_word :
            if char in check : 
                tr = False 
                break
            check.add(char)
        previous_word = char 
    
    if tr :
        cnt += 1


    
print(cnt)