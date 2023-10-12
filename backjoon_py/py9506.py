# 9506 
# 2023-10-12 17:58:24
while(1):
    arr = []
    n = int(input())
    if n == -1:
        break
    m = n
    for i in range(1,n):
        if n % i == 0 :
            arr.append(i)
            m = m - i
    if m == 0:
        print(n,"=",end=" ")
        for i in range(len(arr)):
            print(arr[i], end= " ")
            if i != len(arr)-1 : 
                print("+",end=" ")   
        print()   
    else :
        print(f"{n} is NOT perfect.")
        continue