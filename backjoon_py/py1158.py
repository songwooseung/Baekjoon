import sys

N, K = map(int,sys.stdin.readline().split())

queue = [i for i in range(1,N+1)]
q = []
index = 0

while queue :
    # index가 queue 범위를 같거나 초과할 때 len(queue)로 나눠서 0번째 인덱스부터 원활하게 돌아갈 수 있도록 하자. 
    index = (index + K-1) % len(queue) 
    q.append(queue.pop(index))    
    
print("<",", ".join(map(str,q)),">", sep="") # sep는 값들끼리의 구분자 삽입 (공백)


    