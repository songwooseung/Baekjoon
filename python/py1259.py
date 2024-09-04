import sys

while True : 
    tf = True 
    str = sys.stdin.readline().strip()

    i = 0
    j = len(str)-1
    if str == '0':
        break

    
    for _ in range(0,len(str)//2) : 
        if str[i] != str[j] :
            tf = False
        i += 1 
        j -= 1 
    
    if tf : 
        print("yes")
    else :
        print("no")
