N = int(input())
tf = True 
cnt = 1

pp = [] 
stack = []

# 올바른 수열은 num과 -의 길이가 무조건 동일하게 나옴.
for _ in range(N):
    num = int(input())
    
    # num 이 cnt보다 크거나 같을 때만 실행
    while num >= cnt : 
        stack.append(cnt)
        pp.append('+')
        cnt += 1 # 다음 stack부터 그 다음 숫자부터 시작
        
    if stack[-1] == num :
        stack.pop()
        pp.append('-')
    
    else :
        tf = False

if tf :
    for i in pp :
        print(i)
else :
    print('NO')

