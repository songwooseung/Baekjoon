import sys
input = sys.stdin.readline

word = input().strip()
N = int(input())
cnt = 0

for i in range(N):
    cheak = input().strip()

    if word in cheak :
        cnt += 1
    else :
        for j in range(-len(word)+1,0):
            A = cheak[j:]+cheak[:len(word)+j]
            if A == word :
                cnt += 1
                break

print(cnt)