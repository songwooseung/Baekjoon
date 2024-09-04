# 람다함수 익히기

import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    name, dd, mm, yyyy = input().split()
    dd = int(dd)
    mm = int(mm)
    yyyy = int (yyyy)
    li.append([name,dd,mm,yyyy]) # li.append([name, int(dd), int(mm), int(yyyy)])

li.sort(key = lambda x : (x[3],x[2],x[1]))

# 나이가 작은거부터 출력
print(li[N-1][0]) # print(li[-1][0])
print(li[0][0])
