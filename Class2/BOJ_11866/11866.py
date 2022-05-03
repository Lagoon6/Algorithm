# 요세푸스 class 2
# S4
# list에서 제거X -> 뒤로 넘겨서 순서 지켜나가기
import sys
N,K = map(int,sys.stdin.readline().split())
get_list = []
num_list = [i+1 for i in range(N)]
cnt = K-1

while num_list:
    for i in range(cnt):
        num_list.append(num_list[0])
        num_list.pop(0)
    get_list.append(num_list.pop(0))

print("<",end="")
for i in range(len(get_list)):
    if i == len(get_list)-1:
        print(str(get_list[i])+">",end="")
    else:
        print(str(get_list[i])+", ",end="")

