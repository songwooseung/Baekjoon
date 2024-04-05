import sys # 이거 나중에 다시 풍어보기

stack = []
ps = sys.stdin.readline().strip()
cnt = 0
for i in range(len(ps)):
    if ps[i] == '(':
        stack.append(ps[i])
    else :
        if i>0 and ps[i-1] == '(' :
            stack.pop()
            cnt += len(stack)
        else : 
            stack.pop()
            cnt += 1
print(cnt)