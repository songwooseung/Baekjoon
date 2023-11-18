# 9625
n = int(input()) # 몇 번 바꿀지
a, b = 0,1 # 처음 1을 누를 때 for문을 안돌고 0,1출력
for i in range(1, n): 
    a,b = b, a+b # a는 b로 b는 ba니까 한번 버튼을 누를 때 a는 b, b는 a+b가 된다. (피보나치)
    
print(a,b)
    