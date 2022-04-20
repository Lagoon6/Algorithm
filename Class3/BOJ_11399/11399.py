#11399

import sys
N = int(sys.stdin.readline())
time_list = list(map(int,sys.stdin.readline().split()))
time_list.sort()

for i in range(1,len(time_list)):
    time_list[i] = time_list[i] + time_list[i-1]

sum = 0
for i in range(len(time_list)):
    sum += time_list[i]
print(sum)