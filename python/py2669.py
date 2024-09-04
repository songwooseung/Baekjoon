import sys
# x좌표와 y좌표 모두 1~100까지의 정수를 가지기에 100x100 으로 선언
matrix = [[0] * 100 for i in range(100)] 
cnt = 0 

for _ in range(4) :
    x_i, y_i, x_j, y_j = map(int, sys.stdin.readline().split())

    # input : 1 2 4 4 일 때 
    # x좌표 1,2 / 2,3 / 3, 4 까지의 3개 점 y좌표 2,3 / 3,4 까지 2개 점

    # 여기서 중복 값을 처리해줘야 하니 matrix 값이 0이라면 1로 바꿔서 다음 반복문 때 영향이 가지 않도록 함.  
    for a in range(x_i, x_j) :
        for b in range(y_i, y_j):
            if matrix[a][b] == 0 :
                matrix[a][b] = 1 
                cnt += 1 

print(cnt)