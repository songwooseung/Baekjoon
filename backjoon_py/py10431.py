import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = list(map(int,input().split())) # count에 arr[0], li 변수 만들어서 arr = [1:] 이런 식으로 집어넣어서 사용해도됨.
    
    count = arr[0]
    li = arr[1:]
    total = 0 

    for i in range(0,len(li)): # index 1~19
        for j in range(0, i): # 1 ~ 19
            if(li[i] < li[j]): # 규칙 1 : 자신보다 큰 수가 앞에 없으면 그대로 서고 차례가 끝남
                li[i],li[j] = li[j], li[i]
                total += 1
    print(arr[0],total)
