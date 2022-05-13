
import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in matrix[v]:
        if not visited[i]:
            dfs(i)

N, M = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N)]
visited = [False] * (N)
cnt = 0

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    matrix[u-1].append(v-1)
    matrix[v-1].append(u-1)

for i in range(0 , N ):
    if not visited[i]:
        dfs(i)
        cnt +=1

print(cnt)

