#Class3 
#회의실 배정
import sys

N = int(sys.stdin.readline())
num_list = sorted([tuple(map(int,sys.stdin.readline().split())) for _ in range(N)], key= lambda x:(x[1],x[0]))
#sorted(tuple,key= lambda x: x) -> 튜플 정렬
cnt = 0
end = 0


for s,e in num_list:
    if s>= end:
        cnt +=1
        end = e
print(cnt)
