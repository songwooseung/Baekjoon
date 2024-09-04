# 10813 공 바꾸기
# 2023-10-13 23:31:28
n, m = map(int,input().split())
num = []
for x in range(n):
    num.append(x+1)

'''
다른 방법(1)
num [0] * n # 미리 n개의 배열로 초기화 하는 방법
for x in range(n) : 
    num[x] = x + 1

다른 방법(2)
num[i+1 for i in range(n)] # 이렇게 사용하면 입력된 n에 따라서 적절한 크기의 num 리스트가 생성됨.
'''
    
for x in range (m):
    i, j = map(int,input().split())
    num[i-1], num[j-1] = num[j-1], num[i-1]
    
for x in num : # num의 원소를 x에 하나하나 넣어서 출력하기
   print(x, end=" ")
# for x in range(n) : print(num[x], end=" ")도 가능