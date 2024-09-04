import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# ,를 기준으로 리스트에 하나씩 저장
a = list(map(int, input().split(','))) 
for _ in range(k):
    for i in range(1, len(a)):
        a[i-1] = a[i] - a[i-1]
    a.pop()

# 리스트 a의 모든 요소를 문자여로 반환 후 각 요소를 쉼표로 연결된 하나의 문자열로 만듬
print(",".join(map(str,a)))

# 다른 방법으로는 for i in range(len(a)) 해서 i가 a의 최대 인덱스 크기와 같아질때 
# if문으로 end=""를 써서 ,를 없애줌.