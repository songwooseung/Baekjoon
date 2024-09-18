import sys
# 순열 쓰는 이유, 조합은 순서를 상관안쓰니까 순열을 통해 중복 값 제거해주기
from itertools import permutations 
input = sys.stdin.readline

n = int(input())
k = int(input())

card = []

for i in range(n):
    card.append(input().strip())
# 순열은 중복 값이 있어도 튜플로 순열이 생성 가능함 ex) 1, 1 -> (1,1), (1,1)
# join 쓰는 이유는 2, 1, 13일 때 2113을 만들 수 있고 21,1,3 일때 2113을 만들 수 있기 때문에 만들 수 있는 정수의 개수를 구할땐 중복이 발생할 수 있기에 문자열로 변환 후 중복을 제거한다.
print(len(set("".join(i) for i in permutations(card,k)))) # 순열 i의 집합 크기
