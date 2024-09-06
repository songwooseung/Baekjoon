import sys
import heapq
input = sys.stdin.readline
heap = []

for _ in range(int(input())) :
    x = list(map(int,input().split()))
    if x[0] == 0 :
        if heap : 
            print(-heapq.heappop(heap))
        else :
            print(-1)
    
    else :
        for i in range(1,len(x)) : 
            heapq.heappush(heap,-x[i])