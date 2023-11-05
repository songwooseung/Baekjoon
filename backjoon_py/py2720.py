# 2720
t = int(input())

for i in range(t):
    arr = [0] * 4
    m = int(input())

    arr[0] = m // 25
    m = m % 25
    arr[1] = m // 10
    m = m % 10 
    arr[2] = m // 5
    m = m % 5
    arr[3] = m // 1
    print(arr[0], arr[1], arr[2], arr[3])
     
'''
# 2번째 방법
t = int(input())
for i in range(t):
    m = int(input())
    for j in [25,10,5,1]:
        print(m // j, end=' ')
        m = m % j
    
'''