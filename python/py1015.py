import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

sort_A = A.copy() # sort_A = A는 C의 포인터처럼 배열 sort_A가 A를 가르키게 돼어 둘 중 하나만 값이 바껴도 함께 결과가 반영된다.
sort_A.sort() # 오름차순 정렬

P = [] 
for i in range(N):
    P.append(sort_A.index(A[i])) # 인덱스에 해당하는 배열 값을 P에 넣는 게 아니라, 배열 값에 해당하는 인덱스를 배열에 집어넣음
    sort_A[sort_A.index(A[i])] = -1 # A[i]의 값에 해당하는 sort_A의 인덱스를 찾아 이미 P에 넣은 인덱스는 -1을 해서 중복을 없앰
# print(sort_A) sort_A의 배열 값이 모두 -1로 변했는지 확인

for i in P :
    print(i, end=" ")