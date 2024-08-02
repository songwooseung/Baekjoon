arr = input()
word = ""

for i in arr : 
    if 'A' <= i <= 'Z' : 
        i = ord(i)+13
        if i > 90 :
            i -= 26 # A부터 시작해야하니까
        word += chr(i)
    elif 'a' <= i <= 'z' :
        i = ord(i)+13
        if i > 122 : 
            i -= 26
        word += chr(i)
    else : 
        word += i
print(word)





        