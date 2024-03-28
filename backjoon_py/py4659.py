import sys
input = sys.stdin.readline

while True : 
    password = input().strip()
    if password == 'end':
        break

    vowel = ['a','e','i','o','u']
   
    isTrue = True
    isvowel = False
    con_cnt = 0
    vowel_cnt = 0
    
    for i in range(0, len(password)):
        if password[i] in vowel :
            isvowel = True
            vowel_cnt += 1
            con_cnt = 0
            if vowel_cnt == 3 :
                isTrue = False
                break
        else :
            con_cnt += 1
            vowel_cnt = 0
            if con_cnt == 3 :
                isTrue = False 
                break
        if i > 0 and password[i] == password[i-1] : 
            if password[i] != 'e' and password[i] != 'o' : 
                isTrue = False      
                break

    if isTrue and isvowel :
        print(f'<{password}> is acceptable.')
    else :
        print(f'<{password}> is not acceptable.')
