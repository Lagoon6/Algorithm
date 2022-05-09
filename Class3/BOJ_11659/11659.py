import sys

N, M = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
tmp = 0
new_list = [0]
for num in num_list:
    tmp += num
    new_list.append(tmp)

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    print(new_list[j] - new_list[i-1])