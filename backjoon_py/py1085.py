import sys
input = sys.stdin.readline()

x, y, w, h = map(int,input.split())


print(min(x,y,w-x,h-y)) # x,y (왼쪽, 아래 경계선) w,h (오른쪽, 위 경계선)