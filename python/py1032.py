import sys
imput = sys.stdin.readline

N = int(input())
cmd = []

for i in range(N):
    name = list(input().strip())
    
    if i >= 1 :
        for j in range(len(name)):
            if memory[j] != name[j] :
                memory[j] = '?'
    else :
        # 파이썬의 포인터 개념 기억하기.(첫 lsit name은 memory 값을 참조하기에 memory값이 바뀌면 cmd[0] 값도 같이 바뀜 단, 다음 name부턴 새로운 list이므로 memory값과 연관이 없으므로 cmd[1]부턴 정상적인 name값이 들어감)
        # copy() 함수와 [:] 함수는 동일한 결과를 갖는다.
        memory = name.copy() 

# for i in memory: print(i, end="")
print("".join(memory))