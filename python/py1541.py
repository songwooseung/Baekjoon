import sys
input = sys.stdin.readline

# 문제에서 "가장 처음과 마지막 문자는 숫자이다."라고 했으므로 첫 문자는 무조건 숫자로 시작한다
S = input().strip().split('-')

temp = []
for i in S :
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)

    temp.append(cnt)

result = temp[0] # temp[0]은 그대로 result에 넣는다.

for i in temp[1:]: # 이후 값들은 전부 result에 -해준다.
    result -= i 

print(result)

