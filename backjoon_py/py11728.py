import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A+B
C.sort()

print(' '.join(map(str, C))) # 조인은 문자만 가능 따라서 map함수로 형변환해줌
 