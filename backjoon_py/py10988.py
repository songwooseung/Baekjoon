# 10988 : 팰린드롬인지 확인하기
alphabet = input() 
# length = len(alphabet) # 단어의 길이
tf = True 
for i in range(len(alphabet)//2) : 
    if alphabet[i] != alphabet[len(alphabet)-1-i] :
        tf = False
        break
if tf == True :
    print("1")
else :
    print("0")