# 25642 
import sys
res = ""
A, B = map(int, sys.stdin.readline().split())
while(1) : 
    B += A
    if B > 4 :
        res = "yt"
        break
    A += B
    if A > 4 :
        res = "yj"
        break
print(res)
        
        