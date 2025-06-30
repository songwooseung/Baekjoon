import sys
input = sys.stdin.readline

N = int(input())


# arr[input() for _ in range(N)]
arr = []
for i in range(N) :
    arr.append(input().strip())

# KBS1, KBS2 의 인덱스 번호 추출
idx1, idx2 = arr.index("KBS1"), arr.index("KBS2")

# 내가 쓸 방식은 1,4번만 쓸거임 (올리고 내리기만 있으면 풀이 가능)
# 그리고 KBS1, KBS2가 index[0~1] 순서로 붙어야 있어야 함.

if idx1 > idx2 :
    idx2 += 1

# 해당 문제는 "이미 KBS1이 첫 번째에, KBS2가 두 번째에 있는 입력은 주어지지 않는다."라는 요구사항에 근거한다.
# KBS2는 항상 두번째에 위치해야하나까. idx2-1을 함.
# 문자, 숫자 덧셈 유의
print("1"*idx1+"4"*idx1+"1"*idx2+"4"*(idx2-1))
