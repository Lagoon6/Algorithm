#S4
#비밀번호 찾기
import sys
N, M = map(int,sys.stdin.readline().split())
dic = {}
for _ in range(N):
    site, password = map(str,sys.stdin.readline().split())
    dic[site]=password

for _ in range(M):
    ask = str(sys.stdin.readline().strip('\n'))
    print(dic[ask])
