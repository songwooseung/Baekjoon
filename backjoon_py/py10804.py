import sys
input = sys.stdin.readline

card = [i for i in range(1,21)]

for i in range(10):
    num1, num2 = map(int,input().split())
    div = ((num2 - num1) // 2) + 1
    for j in range(div):
        if num1 != num2 :
            tmp = card[num1-1]
            card[num1-1] = card[num2-1]
            card[num2-1] = tmp
        
        num1 += 1 
        num2 -= 1

for i in card :
    print(i, end=" ")
    

