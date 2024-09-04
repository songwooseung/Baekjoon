# 1037
A = int(input())
arr = list(map(int,input().split()))
arr.sort() 
print(arr[0]*arr[-1]) # 정렬한 값에서 가장 작은 값과 가장 큰 값을 곱하면 N을 구할 수 있다.


# 2번 째 방법 
max = max(arr)
min = min(arr)
print(max * min)    