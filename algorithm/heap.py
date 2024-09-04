import heapq
import sys
input = sys.stdin.readline


# 파이썬 힙의 기본 구조는 최소 힙이다. 
# 최대 힙을 사용하려면 push할 때 -를 넣으면 된다.
# 그렇다면 출력할 떄 -pop을 하여 출력하면 된다.

# 추가로 입력을 받은걸 heap에 넣을 땐 sys.stdin.readline을 사용해야 시간이 매우 절약된다.

heap = []

# 최소 힙 
heapq.heappush(heap,3)
heapq.heappush(heap,2)
heapq.heappush(heap,1)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

# 최대 힙
heapq.heappush(heap,-3)
heapq.heappush(heap,-2)
heapq.heappush(heap,-1)

print(-heapq.heappop(heap))
print(-heapq.heappop(heap))
print(-heapq.heappop(heap))