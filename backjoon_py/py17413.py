# 방법 1 : stack 이용해서 새로운 문자열에 값 집어넣기
# 방법 2 : 인덱스 이용해 start-end 범위 지정해서 그 부분만 reverse 시키기

from collections import deque

# 마지막 ' '를 통해 마지막 출력 가능
S = input() + ' ' 

stack = deque()
result = ''
tf = False

for i in S :
    if i == '<':
        tf = True
        for _ in range(len(stack)):
            result += stack.pop() # < 이전 값들은 반대로 추가
    
    stack.append(i)

    if i == '>' :
        tf = False 
        for _ in range(len(stack)):
            result += stack.popleft() # <> 안의 값이므로 순차적으로 추가
    
    if i == ' ' and tf == False : # ' ' 나오면 그전에 stack 값들 반대로 추가
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

print(result)

''' 방법 2
S = list(input())
i = 0

while i < len(S) :
    if S[i] == '<' :
        while S[i] != '>' :
            i += 1
        
        i += 1 

    elif S[i].isalnum():
        start = i 
        while i < len(S) and S[i] != ' ' and S[i] != '<':
            i += 1 
        tmp = S[start:i]
        tmp.reverse()
        S[start:i] = tmp
    
    elif S[i] == ' ' :
        i += 1 

print(''.join(S))
        
'''

               


