import sys
T = int(sys.stdin.readline())
for _ in range(T):
    stack = []
    ps = sys.stdin.readline().strip()
    
    for i in ps : 
        if stack and (stack[-1] == '(' and i == ')') :
            stack.pop() 
        else :
            stack.append(i)
    
    if stack :
        print("NO")
    else :
        print("YES")