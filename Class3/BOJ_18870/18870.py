import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
sort_list = sorted(list(set(num_list)))
dic = {}

for i in range(len(sort_list)):
    dic[sort_list[i]] = i

for i in num_list:
    print(dic[i], end=" ") 