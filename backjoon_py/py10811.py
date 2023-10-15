#10811 : 바구니 뒤집기
n, m = map(int,input().split())
i = 0
j = 0
arr = [i+1 for i in range(n)] # 1 2 3 4 5
for x in range(m):
    i, j = map(int,input().split())
    cnt = 0
    
    for y in range(i,j):
        arr[y-1],arr[j-1-cnt] = arr[j-1-cnt],arr[y-1] #인전한 방이 아니면 cnt를 추가해서 더 빼줌
        cnt += 1
        if y > j-1-cnt : # arr[1]와 arr[2]를 교환한 후 arr[2]와 arr[1] 교환을 방지하기 위함. -> 두 번 교환 방지
            break

for x in arr:
    print(x,end=" ") 
'''
for x in range(n):
    print(arr[x],end=" ")
'''  