#토마토
#GOLD 5 
from collections import deque
import sys

M, N, H = map(int,sys.stdin.readline().split())
matrix = [[list(map(int,input().split())) for i in range(N)] for _ in range(H)]
queue = deque()
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
res = 0

for h in range(H):
    tmp = matrix[h]
    for n in range(N):
        for m in range(M):
            if tmp[n][m] ==1:
                queue.append([h,n,m])

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):  
            nx, ny, nz = dx[i]+x, dy[i] + y, dz[i]+z
            if 0<=nx < H and 0 <= ny < N and 0<= nz < M and matrix[nx][ny][nz] ==0: 
                matrix[nx][ny][nz] = matrix[x][y][z] +1  
                queue.append([nx,ny,nz]) 
bfs()

for high in matrix:
    for row in high:
        for col in row:
            if col == 0:
                print(-1)
                exit(0)
        res = max(res,max(row))
print(res-1)

