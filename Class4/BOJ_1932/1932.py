import sys

n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
    k = list(map(int,sys.stdin.readline().split()))
    num_list.append(k)

cnt = 2
for i in range(1,n):
    for j in range(cnt):
        if j == 0:
            num_list[i][j] = num_list[i][j]+num_list[i-1][j]
        elif i == j:
            num_list[i][j] = num_list[i][j]+num_list[i-1][j-1]
        else:
            num_list[i][j] = max(num_list[i-1][j-1],num_list[i-1][j])+num_list[i][j]
        
    cnt +=1
print(max(num_list[n-1]))