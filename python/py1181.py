import sys
N = int(sys.stdin.readline())

word = [] 

for _ in range(N):
    word.append(sys.stdin.readline().strip())
word = list(set(word))

word.sort() # 알파벳 순서로 우선 정렬
word.sort(key=len) # 문자열 길이 순으로 정렬

for i in word:
    print(i)

# 결과는 동일하지만 시간초과가 뜬 코드
'''
for i in range(len(word)):
    for j in range(i+1,len(word)):
        if len(word[i]) == len(word[j]):
            for k in range(len(word[i])):
                if (ord(word[i][k])) > ord((word[j][k])): # 문자를 아스키코드값으로 바꿔서 계산해줌
                    tmp = word[i]
                    word[i] = word[j]
                    word[j] = tmp 
                    break
        elif len(word[i]) > len(word[j]):
            tmp = word[i]
            word[i] = word[j]
            word[j] = tmp 

for i in word :
    print(i)
'''