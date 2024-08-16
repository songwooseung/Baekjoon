# 1251 단어 나누기

word = input()
result = []

for i in range(1,len(word)): # 1 2 3 4 
    for j in range(i+1,len(word)): # 2 3 4 5 6/ 3 4 5 6/ 4 5 6 / 5 6 / 5 
        word1 = word[:i][::-1]
        word2 = word[i:j][::-1]
        word3 = word[j:][::-1]
        result.append(word1+word2+word3)

# sorted는 새로운 배열 값을 담고 있음 result값 자체 변경 X 
print(sorted(result)[0]) # 자체가 리스트로 반환