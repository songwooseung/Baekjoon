# 2798 : 블랙잭
N, M = map(int,input().split())
card = list(map(int,input().split()))
# card.reverse() # 내림차순 정렬을 하면 for문을 한번만 돌려도 됨 왜냐하면 card[0]은 가장 큰 값이기 때문
sum = 0
for i in range(N) :
    for j in range(i+1,N):
        for k in range(j+1,N):
            if card[i]+card[j]+card[k] <= M :
                sum = max(sum, card[i]+card[j]+card[k]) # 기존의 sum과 비교하여 큰 값을 sum에 저장
print(sum)