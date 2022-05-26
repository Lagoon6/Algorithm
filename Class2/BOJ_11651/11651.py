import sys

n = int(sys.stdin.readline())
num_list= [ []*i for i in range(n)]

for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    num_list[i].append(y)
    num_list[i].append(x)
num_list.sort()

for i in range(len(num_list)):
    print(num_list[i][1], num_list[i][0])