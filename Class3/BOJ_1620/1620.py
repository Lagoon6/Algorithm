import sys

N, M = map(int,sys.stdin.readline().split())

dic = {}
for i in range(N):
    pocketmon = sys.stdin.readline().rstrip()
    dic[pocketmon] = i+1
dic2 = {v:k for k,v in dic.items()} #딕셔너리 뒤집기
for j in range(M):
    cmd = sys.stdin.readline().rstrip()
    if dic.get(cmd, 0 ) == 0:
        cmd = int(cmd)
        print(dic2[cmd])
    else:
        print(dic[cmd])
