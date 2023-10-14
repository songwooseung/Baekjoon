# 3052
# 2023-10-15 01:46:08
arr = [0] * 10
cnt = 0
for i in range(10):
    arr[i] = int(input())
    arr[i] %= 42 
    
for i in range(len(arr)): # len(arr)-1 해줘야하지만 애초에 i가 9가 되도 j는 10부터 시작하기 때문에 for문을 탈출한다. 
    for j in range(i+1,len(arr)):
        if(arr[i] == arr[j]):
            cnt += 1 
            break # j for문 탈출 i를 기준으로 1개씩만 카운트해야하니까. 
print(len(arr)-cnt)
        

    