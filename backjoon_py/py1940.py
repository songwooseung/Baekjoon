# 투포인터

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = sorted(list(map(int,input().split())))
left, right = 0, len(arr)-1
cnt = 0

while left < right :
    sum_num = arr[left] + arr[right]

    if sum_num < M :
        left += 1
    elif sum_num > M :
        right -= 1 
    # 고유 번호를 더하면 다신 그 번호를 사용하지 못한다. (중복이 안되는 고유 번호)
    else :
        cnt += 1
        left += 1 
        right -= 1 

print(cnt)


    