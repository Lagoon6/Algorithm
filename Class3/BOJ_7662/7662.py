import sys
import heapq


T = int(sys.stdin.readline())
heap = []

for _ in range(T):
    k = int(sys.stdin.readline())
    for _ in range(k):
        cmd = list(sys.stdin.readline().split())
        cmd[1] = int(cmd[1])
        if cmd[0] == 'I':
            heapq.heappush(heap,cmd[1])
        elif cmd[0] == 'D':
            if cmd[1] == 1:
                if len(heap) == 0:
                    continue
                else:
                    heap = heapq.nlargest(len(heap),heap)[1:] #최대값 제거
                    heapq.heapify(heap)
            elif cmd[1] == -1:
                if len(heap) == 0:
                    continue
                else:
                    heapq.heappop(heap) #최소값 제거
                    
    if len(heap) == 0:
        print('EMPTY')
    else:
        print(heapq.nlargest(len(heap),heap)[0],heapq.heappop(heap))
