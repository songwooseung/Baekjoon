arr = input()
S = set()
k = 0

while k < len(arr) :

    for i in range(len(arr)-k):
        j = i
        if arr[i:j+1+k] not in S : 
            S.add(arr[i:j+1+k]) 
    k += 1

print(len(S))

'''
# 외부 코드 
s=input()
total=set()
for i in range(len(s)):
    for j in range(i,len(s)):
        total.add(s[i:j+1]) # 다 집어넣어서 중복을 없애주는 방법 
    
print(len(total))
'''