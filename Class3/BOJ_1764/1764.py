#dic or set 탐색
#이진분류 -> str 탐색 힘듬 
import sys

N, M = map(int,sys.stdin.readline().split())

dic = {}

for i in range(N+M):
    input = sys.stdin.readline()
    if input not in dic:
        dic[input] = 1
    else:
        dic[input] = 2

result_list = []
for input in dic.items():
    if input[1] == 2:
        result_list.append(input[0])
print(len(result_list))
result_list.sort()
for i in range(len(result_list)):
    print(result_list[i].strip('\n'))