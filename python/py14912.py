import sys
input = sys.stdin.readline

# .count() -> 문자열 또는 리스트에서 빈도수를 알려줌
N, M = map(int,input().split())
digit = 0
for i in range(1,N+1):
    digit += str(i).count(str(M))

print(digit)


