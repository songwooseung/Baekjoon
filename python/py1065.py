N = int(input())
hansu = 0
for i in range(1,N+1):
    arr = list(map(int,str(i)))
    if i < 100 :
        hansu += 1
    elif arr[0]-arr[1] == arr[1]-arr[2]:
        hansu += 1

    
