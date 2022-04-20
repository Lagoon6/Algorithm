import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

num_list = [ i+1 for i in range(N)]
get_list = []
cnt = K-1
while len(num_list)>0:
    get_list.append(num_list.pop(cnt))
    cnt = cnt + K
    

[1,2,3,4,5,6,7]

    