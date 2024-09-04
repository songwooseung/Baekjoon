import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    wears = {}

    # 아무 옷도 입지 않는 경우도 하나의 경우의 수로 포함, 곱해야함 그라고
    cnt = 1

    for i in range(N):
        wname, wtype = input().strip().split()
        
        if wtype in wears : 
            wears[wtype].append(wname)
        else :
            # 리스트 형태로 초기화 시켜줘야함.
            wears[wtype] = [wname]
    
    for x in wears :
        # wears[x] : 해당하는 의상 종류의 옷 개수
        # 1을 더한 이유는 아무 옷도 입지 않은 경우의 수를 포함한 결과
        cnt *= len(wears[x])+1

    # 의상을 입지 않은 모든 경우의 수를 출력
    print(cnt-1)


