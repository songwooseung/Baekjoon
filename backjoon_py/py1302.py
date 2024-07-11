import sys
input = sys.stdin.readline


N = int(input())

arr = dict()

for i in range(N):
    book = input().strip()   
    if book not in arr :
        arr[book] = 1 
    else : 
        arr[book] += 1 


# 내림차순 : x를 -로 바꿔서 정렬을 역으로 바꿈.
# 1차 기준은 값을 기준으로 2차 기준은 책 제목을 기준으로  
arr2 = sorted(arr.items(),key=lambda x : (-x[1],x[0]))

print(arr2[0][0])