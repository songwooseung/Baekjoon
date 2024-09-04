import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []

for i in range(N):
    arr.append(list(input().strip())) # \n 제거

# print(arr)
result = '' # dna 최대 빈도수
cnt = 0 # Hamming Distance의 합 

for i in range(M):
    dna = [0,0,0,0] # a, c, g, t -> 사전순
    for j in range(N): 
        if arr[j][i] == 'A': # 각 행의 첫 번째 열부터 비교해주기
            dna[0] += 1 
        elif arr[j][i] == 'C':
            dna[1] += 1 
        elif arr[j][i] == 'G':
            dna[2] += 1 
        elif arr[j][i] == 'T':
            dna[3] += 1
    
    # 1번 째 방법
    if max(dna) == dna[0]: # 빈도수가 겹치더라도 사전 순으로 가장 앞서는 것을 출력하므로 A부터 먼저 비교한다.
        result += 'A'
        cnt += dna[1] + dna[2] + dna[3]
    elif max(dna) == dna[1]:
        result += 'C'
        cnt += dna[0] + dna[2] + dna[3]
    elif max(dna) == dna[2]:
        result += 'G'
        cnt += dna[0] + dna[1] + dna[3]
    elif max(dna) == dna[3]:
        result += 'T'
        cnt += dna[0] + dna[1] + dna[2]
    
    '''
    # 2번 째 방법
    idx = dna.index(max(dna)) # 가장 큰 값이 있는 dna값의 인덱스를 가져옴
    
    if idx == 0 :
        result += 'A'
    elif idx == 1  : 
        result += 'C'
    elif idx == 2  : 
        result += 'G'
    elif idx == 3  : 
        result += 'T'
    cnt += N - max(dna)
    '''
print(result)
print(cnt)
