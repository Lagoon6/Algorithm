import sys
from collections import deque

def bfs(graph, start):
    num = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

N, M = map(int,sys.stdin.readline().split())
graph = [[]*i for i in range(N+1)]
res = []
for i in range(M):
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(1,N+1):
    res.append(bfs(graph,i))
print(res.index(min(res))+1)


    
