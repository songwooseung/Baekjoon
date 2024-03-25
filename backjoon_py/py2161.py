import sys
input = sys.stdin.readline

N = int(input())

# arr1 = list(map(int,input().split())) -> 리스트를 사용자가 입력해서 넣을 때 
arr1 = list(map(int,range(1,N+1))) # -> map함수를 이용해 1~N까지 순서대로 배열에 넣기
arr2 = []

while (len(arr1) > 1) :
    arr2.append(arr1.pop(0)) # -> 이렇게 써도 arr1의 0번째 index가 삭제됨.

    if(len(arr1) == 1) : 
        break

    val = arr1[0]
    for i in range (0,len(arr1)-1):
        if val == arr1[i] :
            tmp = arr1[i]
            arr1[i] = arr1[i+1]
            arr1[i+1] = tmp

for i in arr2 :
    print(i, end=" ")
print(arr1[0])