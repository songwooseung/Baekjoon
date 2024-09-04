A, B = input().split()

# 최소 차이를 구하는 배열 선언
result = []

# A와 B의 길이가 같을 수도 있기 때문에 +1을 해서 for문이 무조건 돌아갈 수 있도록 해줌
for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    result.append(cnt)

print(min(result))
