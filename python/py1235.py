import sys
input = sys.stdin.readline 

N = int(input())

code = [input().strip() for i in range(N)]
cnt = 0 

for i in range(1, len(code[0])+1): # -1 ~ -7 역순
    fixed = set()

    for j in code :
        # 리스트 슬라이스 : ['34', '56'], 문자열 슬라이스 : "45","56" 
        # 파이썬에서 배열과 1차원 리스트는 비슷해보이지만, np.array를 통해 확실하게 배열로 선언 가능.
        # 배열 -> 리스트 변환 O
        # 리스트 -> 집합 변환 X
        fixed.add(j[-i:])
    
    if len(fixed) == N :
        cnt = i
        break

print(cnt)
        
