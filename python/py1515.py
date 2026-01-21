# 백준 1515번 수이어쓰기
import sys
input = sys.stdin.readline

S = input().strip()
idx = 0
k = 1

while idx < len(S) :
    a = str(k)

    for b in a :
        # idx <len(S) 부터 안하면 바로 S[idx] == b 비교해서 index 에러 생김
        if idx < len(S) and S[idx] == b : 
            idx += 1
    
    k += 1

print(k-1)






    


