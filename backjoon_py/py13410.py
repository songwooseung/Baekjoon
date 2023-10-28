import sys
arr = []
N, K = map(int, sys.stdin.readline().split())
print("바뀌기전")
for i in range(1, K+1):
    arr.append(N*i)
    print(arr[i-1], end=" ") 
print()
print("바뀌고 난 후")
for i in range(0, K):
    if(arr[i] >= 10):
        arr[i] = int(str(arr[i])[::-1]) # str(arr[i])를 통해 arr[i]를 문자열로 바꿔주고 [::-1]을 통해 문자열을 뒤집어준 후 int형으로 바꿔줌
    print(arr[i], end=" ")
print()
print("가장 큰 값 =",max(arr))
        
        