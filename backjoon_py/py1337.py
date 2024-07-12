import sys
input = sys.stdin.readline

N = int(input())
arr = [] 
for _ in range(N):
    arr.append(int(input()))

arr.sort()

start = 0 
max_num = 0

for end in range(N):

    # 5개의 연속된 수를 나타내기 위해선 start와 end의 차가 5 이상이여선 안됨.
    while arr[end] - arr[start] > 4 :
        start += 1
    # 연속된 배열의 요소가 0부터 시작하니 + 1을 해줌
    max_num = max(max_num, end-start+1) 

# 만약 5개의 원소가 연속적이면 결과는 그대로 5-5 = 0로 출력될 것이다.
print(5-max_num) 





