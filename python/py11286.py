import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())) :
    x = int(input())

    if x != 0 :
        # (정수,정수)로 저장되어 [0] 기준으로 우선순위를 가진다. 
        # 우선 순위가 같으면 [1] 에서 더 작은 값을 기준으로 출력이 된다 (heapq는 기본 Min-heap)
        heapq.heappush(heap,(abs(x),x))
    
    else :
        if heap :
            print(heapq.heappop(heap)[1])
        
        else : 
            print(0)