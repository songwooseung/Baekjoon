import sys
input = sys.stdin.readline


c_word = input().strip()
cnt = 0
i = 0


while i < len(c_word) :
    if i+1 < len(c_word):
        if c_word[i] == 'c':
            if c_word[i+1] == '=':
                cnt += 1
                i+=2
                continue
            elif c_word[i+1] == '-':
                cnt += 1
                i+=2
                continue
        elif c_word[i] == 'd':
            if c_word[i+1:i+3] == "z=":
                cnt +=1
                i+=3
                continue
            elif c_word[i+1] == '-':
                cnt+=1
                i+=2
                continue
        elif c_word[i] == 'l':
            if c_word[i+1] == 'j':
                cnt+=1
                i+=2
                continue
        elif c_word[i] == 'n':
            if c_word[i+1] == 'j':
                cnt+=1
                i+=2
                continue
        elif c_word[i] == 's':
            if c_word[i+1] == '=':
                cnt+=1
                i+=2
                continue
        elif c_word[i] == 'z':
            if c_word[i+1] == '=':
                cnt+=1                
                i+=2
                continue
    
    cnt += 1
    i += 1
        
print(cnt)
    




