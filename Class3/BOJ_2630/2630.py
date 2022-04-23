import sys

N = int(sys.stdin.readline())
map_list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = []

def solution(x, y, N) :
  color = map_list[x][y] # 0 or 1의 값
  for i in range(x, x+N) : # N = 8 
    for j in range(y, y+N) :
      if color != map_list[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))
