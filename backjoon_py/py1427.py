# 문제 : 1427 소트인사이드 
# 해설 : 수를 입력받아 각 자릿수를 내림차순으로 정렬하는 알고리즘 

import sys

N = sys.stdin.readline().strip()
cnt = 0 
li = []

while(cnt < len(N)) :
    li.append(int(N[cnt]))
    cnt += 1

li.sort(reverse=True)

for i in li :
    print(i, end="")


