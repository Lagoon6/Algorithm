import sys

n, k = map(int,sys.stdin.readline().split())
coin_list = []

for _ in range(n):
    coin_list.append(int(sys.stdin.readline().rstrip()))

coin_list.sort(reverse=True)
cnt = 0
for i in range(len(coin_list)):
    r = k//coin_list[i]
    k = k%coin_list[i]
    cnt += r
print(cnt)
