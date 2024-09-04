import sys
input = sys.stdin.readline
'''
설명
: 패스워드 검색을 해야한다. 
O(n*m)으로 간단하게 구현할 수 있지만 시간초과가 뜨는 관계로
딕셔너리를 이용해 문제를 풀어야한다.

'''
# 딕셔너리 

N, M = map(int, input().split())
password = {}

for _ in range(N):
    pas, id = input().split()
    password[pas] = id # pas로 검색을 하면 값으로 id가 추출된다.

for _ in range(M):
    search = input().strip('\n')
    print(password[search])
    
'''
-> 정답이지만 시간초과가 나는 비효율적인 코드

N, M = map(int, input().split())
password = []
pas = []
for i in range(N):
    pw, id = input().split()
    password.append((pw,id))

for i in range(M):
    search = input().rstrip('\n')

    for j in range(N):    
        if password[j][0] == search :
            pas.append(password[j][1])
            break

for i in pas:
    print(i)
'''    

