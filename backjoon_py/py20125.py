import sys
input = sys.stdin.readline

N = int(input())
board = [list(input()) for _ in range(N)]

x, y = -1,0
for i in range(N):
    for j in range(N):
        if(x == -1):
            if(board[i][j] == '*'):
                x = i+2
                y = j+1
                #print("머리 좌표 : %d,%d]" %(x,y))
                break
    if x != -1:
        break

# 왼쪽 팔 길이 구하기
left_arm = 0
for j in range(y-1):
    if board[x-1][j] == '*':
        left_arm += 1
#print(f'left_arm : {left_arm}')

# 오른쪽 팔 길이 구하기 
right_arm = 0
for j in range(y,N):
    if board[x-1][j] == '*':
        right_arm += 1
    else :
        break
#print(f'right_arm : {right_arm}')

# 허리 길이 구하기
waist = 0
for i in range(x,N):
    if board[i][y-1] == '*':
        waist += 1
    else :
        break
#print(f'waist : {waist}')

# 왼쪽 다리 길이 구하기  
left_leg = 0
for i in range(x+waist-1,N):
    if board[i][y-2] == '*':
        left_leg += 1
#print(f'left_leg : {left_leg}')

# 오른쪽 다리 길이 구하기 
right_leg = 0
for i in range(x+waist-1,N):
    if board[i][y] == '*':
        right_leg += 1
#print(f'right_leg : {right_leg}')
    
print(x,y)
print(left_arm,right_arm,waist,left_leg,right_leg, end=" ")



             