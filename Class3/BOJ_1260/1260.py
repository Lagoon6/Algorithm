#Class3 Siver2
#DFS & BFS
import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())
graph= [[0]*(N+1) for _ in range(N+1)]
visit_list = [0]*(N+1)
visit_list2 = [0]*(N+1)
def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v, end= " ")
        for i in range(1,N+1):
            if visit_list[i] ==0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1
def dfs(v):
    visit_list2[v] =1
    print(v,end = " ")
    for i in range(1, N+1):
        if visit_list2[i] ==0 and graph[v][i] == 1:
            dfs(i)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] =1
dfs(V)
print()
bfs(V)