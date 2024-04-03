# 존나 어거지로 품
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))

queue = []
t = 0
i = 0

while True :
    if P[i] != 0 :
        t += 1
        queue.append(i+1)
        P[i] -= 1

    i += 1

    if i % N == 0 :
        i = 0
     
    if max(P) == 0:
        break


# print(queue)

for i in range(N):
    for j in range(t):
        if (i+1) == queue[j] :
            P[i] = (j+1)

    print(P[i],end=" ")
print()
