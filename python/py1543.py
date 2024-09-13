import sys
input = sys.stdin.readline

word = input().strip()
find = input().strip()

cnt = 0
index = 0


for i in range(len(word)):

    # 중복 부분 걸러내기 위함
    if index > i :
        continue

    # i번째부터 비교하기 위함
    if find == word[i:i+len(find)] : 
        cnt += 1 

        index = i+len(find)


print(cnt)