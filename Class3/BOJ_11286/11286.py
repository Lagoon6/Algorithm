#Silver 1
#heap 최소 최대 -> heap -,+ 만들 생각
#abs -> 절대값

import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
plus_heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x < 0:
        heapq.heappush(min_heap,(-x,x))
    elif x > 0:
        heapq.heappush(plus_heap,x)
    else:
        if len(min_heap) ==0 and len(plus_heap) != 0:
            print(heapq.heappop(plus_heap))
        elif len(plus_heap) == 0 and len(min_heap) != 0:
            result = heapq.heappop(min_heap)
            print(result[1])
        elif len(plus_heap) ==0 and len(min_heap) == 0:
            print(0)
        elif len(plus_heap) != 0 and len(min_heap) != 0:
            if abs(min_heap[0][1]) > plus_heap[0]:
                print(heapq.heappop(plus_heap))
            elif abs(min_heap[0][1]) < plus_heap[0]:
                result = heapq.heappop(min_heap)
                print(result[1])
            elif abs(min_heap[0][1]) == plus_heap[0]:
                result = heapq.heappop(min_heap)
                print(result[1])



