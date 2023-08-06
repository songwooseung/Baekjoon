t = int(input())

for i in range(0,t):
    arr = [0] * 10
    
    arr = list(map(int,input().split()))
    arr.sort()
    print(arr[7])
            