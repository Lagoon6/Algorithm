#_7662
#class3 gold4
#heapq 활용 + visited 인덱스 -> 포인터느낌으로 사용하기

import sys
import heapq
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    visitied = [False]*1000001 #visited를 따로만들어서 두는게 중요함
    min_heap,max_heap = [],[]
    for i in range(k):
        cmd = list(sys.stdin.readline().split())
        if cmd[0] == 'I':
            heapq.heappush(min_heap,(int(cmd[1]),i))
            heapq.heappush(max_heap,(-int(cmd[1]),i))
            visitied[i] = True  
        else:
            if cmd[1] == "-1":
                while min_heap and not visitied[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap: 
                    visitied[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            if cmd[1] == "1":
                while max_heap and not visitied[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visitied[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visitied[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visitied[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if len(min_heap)==0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])