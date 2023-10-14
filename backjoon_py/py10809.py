# 10809 : 알파벳 찾기
S = input()
arr = [-1] * 26 # arr = [-1 for i in range(26)] 도 가능
for i in range(len(S)) :
    if arr[ord(S[i])-97] == -1 : # 처음 등장하는 위치니까 -1일 때 추가
        arr[ord(S[i])-97] = i
for i in range(len(arr)) :
    print(arr[i], end=" ")