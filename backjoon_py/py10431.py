import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = list(map(int,input().split())) # count에 arr[0], li 변수 만들어서 arr = [1:] 이런 식으로 집어넣어서 사용해도됨.
    
    count = arr[0]
    li = arr[1:]
    total = 0 

    for i in range(0,len(li)): # index 0 ~ 19
        for j in range(0, i): # 0 ~ 18 -> 어차피 i,j비교라 마지막 인덱라는 i만 해당하면 됨
            if(li[i] < li[j]): 
                li[i],li[j] = li[j], li[i]
                total += 1
    print(count,total)
