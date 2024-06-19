import sys

stack = [] 

def insert(x):
    stack.append(x)
def delete() :
    if stack :
        return print(stack.pop())
    else :
        print(-1)

def length():
    print(len(stack))

def isempty():
    if stack : 
        print(0)
    else :
        print(1)

def head():
    if stack :
        print(stack[-1])
    else :
        print(-1)

T = int(sys.stdin.readline())


for _ in range(T):
    n = sys.stdin.readline().split() # 문자형 배열로 입력받아서 처리해주기 

    if(n[0] == "1"):
        insert(int(n[1]))
    elif(n[0] == "2"):
        delete()
    elif(n[0] == "3"):
        length()
    elif(n[0] == "4"):
        isempty()
    elif(n[0] == "5"):
        head()
