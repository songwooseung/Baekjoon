# 8958
# 2023-10-14 14:34:08
n = int(input())

for i in range(n):
    arr = [] 
    cnt = 0
    sum = 0
    arr = list(input()) 
    # arr.append(list(input())), 즉 append에 list를 넣는 것은 말그대로 list 자체를 arr리스트 안에 넣는 다는 뜻이다.
    # 그렇기 때문에 arr[i][j]같은 이차원 배열을 사용하는 것이 아니라면 list(input())을 써야한다.
    # list()로 선언하면 값을 한 방씩 잘라서 넣어준다.
    # split()은 공백 구분이므로 문자를 OXOXO처럼 받으면 공백이 없기 때문에 하나의 방에 들어간다.
    for j in range(len(arr)):
        if arr[j] == 'O':
           cnt = cnt + 1
           sum += cnt
        else:
            cnt = 0
    print(sum)


            
    