import sys 
input = sys.stdin.readline

N = int(input())
binary = bin(N)[2:]
exp = len(binary)-1
res = 0

for i in binary :
    if int(i) :
        res += 3 **exp
    exp -= 1 # 다음 턴으로 넘어갈 때마다 제곱수를 1씩 줄임

print(res)