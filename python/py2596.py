import sys
input = sys.stdin.readline

N = int(input())
string = input().strip()

secret = ['000000','001111','010011','011100','100110','101001','110101','111010']
arr = []
cor = ''


for i in range(0,len(string),6):
    arr.append(string[i:i+6])

for i in arr :
    wrong = 0
    for j in secret :
        cnt = 0 # i를 기준으로 j번 반복하기 위함.
        for k in range(6):
            if i[k] == j[k] :
                cnt += 1

        if cnt >= 5 :
            cor += chr(secret.index(j) + 65) # secret에 있는 j값에 해당 하는인덱스에 65 더하여 문자로 변환
            break
        else : # 두 글자 이상 다를 때 (cnt < 5)
            wrong += 1 
    
    if wrong == len(secret) : # 문자가 A~H까지 총 8개 있으니까 secret을 기준으로 함
        print(arr.index(i) + 1)
        quit()

print(cor)
            

