while True:
    word = input()
    if word[0] == '.':
        break

    stack = []

    for char in word:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        elif char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)

    if not stack:
        print('yes')
    else:
        print('no')


