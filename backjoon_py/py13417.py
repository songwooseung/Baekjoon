import sys
from collections import deque
input = sys.stdin.readline

'''
# 방법 1 
# t = int(input())

# for _ in range(t) : 
#     num = int(input())
#     card = deque(map(str,input().split()))
#     result = deque(card.popleft())
    
#     while card : 
#         if result[0] < card[0] : # 문자/문자 비교 -> 아스키 코드 값으로 비교 
#             result.append(card.popleft())
#         else :
#             result.appendleft(card.popleft())

#     print(*result, sep="")  # 구분자
'''

# 방법 2 - 시간은 비슷
for _ in range(int(input())):
    num = int(input())
    card = list(map(str,input().split()))
    word = deque(card[0])

    for i in card[1:] : # card[1] 부터 넣겠다.
        if word[0] >= i :
            word.appendleft(i)
        else :
            word.append(i)

    
    print(*word,sep="")



