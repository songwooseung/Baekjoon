# python/heap 메소드 
# 기본 형식 : heapq.//(힙변수)
# heappush, heappop 방식
# python에서 maxheap은 지원하지 않으므로 push에서 -를 삽입해 maxheap 구현 (출력시 -는 heappop만 가능) 

import sys
import heapq
input = sys.stdin.readline

N = int(input())
max_heap = []

for _ in range(N):
    x = int(input())
    if x == 0 :
        if max_heap :
            print(-heapq.heappop(max_heap))
        else : 
            print(0)
    else :
        heapq.heappush(max_heap,-x)

    