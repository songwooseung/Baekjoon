import sys

input = sys.stdin.readline

S = set()
N = int(input())

for i in range (N):
    # op[0],[1]을 각각의 변수에 집어넣어서 쓰면 코드 가독성이 더 좋을 듯? (맨 아래 남의 코드 참조)
    op = input().split()

    if op[0] == "all" :
        S.update(i for i in range(1,21)) # 재선언 vs. update는 메모리 재사용 측면에서 update가 더 낫다고 한다.
    elif op[0] == "empty" :
        S.clear()

    elif op[0] == "add" :
        S.add(int(op[1]))
    elif op[0] == "remove" :
        if int(op[1]) in S :
            S.remove(int(op[1]))
    elif op[0] == "check":
        if int(op[1]) in S:
            print(1)
        else : 
            print(0)
    elif op[0] == "toggle" :
        if int(op[1]) in S:
            S.remove(int(op[1]))
        else : 
            S.add(int(op[1]))

"""
import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)


"""