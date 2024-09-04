# 2566번: 최댓값
# 2023-10-12 06:09:10
max = 0
arr = []
idx_i = 0
idx_j = 0

for i in range(9):
    arr.append(list(map(int,input().split())))  
    # split을 통해 공백을 기준으로 나누어진 값들을 int()함수를 통해 정수형으로 변환하여 arr에 append함
    # list() 함수는 입력받은 값을 리스트로 만들어주는 함수이다. -> for문이 돌아가는 동안 입력받은 값들은 서로 다른 행에 저장된다.
for i in range(9):
    for j in range(9):
        if arr[i][j] > max :
            max = arr[i][j]
            idx_i = i
            idx_j = j
print(max)
print(idx_i+1,idx_j+1)