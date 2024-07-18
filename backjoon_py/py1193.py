import sys 
input = sys.stdin.readline

# 찾고 싶은 n번째 분수
num = int(input())

line = 1

# num - line을 반복해주면 찾고 싶은 n번째 분수의 라인을 찾을 수 있다.
while line < num :
    num -= line
    line += 1 

if line % 2 == 0:
    a = num
    b = line - num + 1 

else :
    a = line - num + 1
    b = num

print(f'{a}/{b}')
