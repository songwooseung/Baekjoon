word = input()
stack = []

for char in word :
    if char == '(' :
        stack.append(char) 
    elif char == ')' :
        if stack and stack[-1] == '(' :
            stack.pop()
        else : 
            stack.append(char)
    
print(len(stack))