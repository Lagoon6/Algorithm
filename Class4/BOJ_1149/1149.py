#_1149
#_DP Silver1 
#_누적에서 합하기 
import sys

N = int(sys.stdin.readline())
rgb = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

#rgb[i][0] == 빨간집
#rgb[i][1] == 초록집
#rgb[i][2] == 파란집

for i in range(1,N):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])
print(min(rgb[N-1]))