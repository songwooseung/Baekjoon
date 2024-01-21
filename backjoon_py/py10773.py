# -*- coding: utf-8 -*-

# 방법 1
# 수를 입력받고 배열에 append 또는 pop하기
# pop()은 마지막 배열의 방을 삭제함

# 코드 ----------------------------------
# N = int(input())
# arr = []

# for i in range(0,N):
#     num = int(input())
#     if num == 0 :
#         arr.pop()
#     else :
#         arr.append(num)
# print(sum(arr)) # sum 함수는 배열의 값들을 모두 더해줌

# 방법 2 -> 배열에서 del하기

# 코드 ----------------------------------
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
arr = [0] * (N+1)

for _ in range(0, N) : 
    arr[cnt] = int(input())
    if arr[cnt] == 0 :
        del arr[cnt-1]
        del arr[cnt]
        cnt -= 1
    else : cnt += 1
    
print(sum(arr))