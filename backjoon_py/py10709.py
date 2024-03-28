import sys
input = sys.stdin.readline

H, W = map(int,input().split())
arr = []
arr2 = [[-1 for i in range(W)] for j in range(H)]

for i in range(H):
    # split은 공백을 기준으로 입력을 분리하기 때문에, 사용 X
    # strip()을 통해 공백을 제거하여 문자열의 \n 제거 가능
    arr.append(list(map(str,input().strip()))) 

# print(arr)
# print(arr2)

for i in range(H):
    isTrue = False
    num = 1
    for j in range(W):
        if arr[i][j] == 'c':
            isTrue = True
            arr2[i][j] = 0
            num = 1
        elif isTrue : 
            if arr[i][j] == '.':
                arr2[i][j] = num
                num += 1
        else :
            arr2[i][j] = -1
            isTrue = False

                
for i in range(H):
    for j in range(W):
        print(arr2[i][j], end=" ")
    print()
