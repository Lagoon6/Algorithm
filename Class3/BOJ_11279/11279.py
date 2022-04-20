# heap -> 우선순위 최대힙

import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(heap) ==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-x,x))

