S = input()
cnt = 0 

# 연속된 문자가 다르면 cnt + 1 마지막에 cnt + 1을 한 상태에서 2를 나눠주면 최소 횟수가 나옴 
for i in range(len(S)-1):
    if S[i] != S[i+1] :
        cnt += 1 
print((cnt+1) // 2)
