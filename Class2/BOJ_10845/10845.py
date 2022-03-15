#SILVER 4 
#queue
import sys
N = int(sys.stdin.readline())

queue = []
for i in range(N):
    k = sys.stdin.readline().split()
    if k[0] == "push":
        queue.append(k[1])
    elif k[0] == "front":
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[0])
    elif k[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif k[0] == "size":
        print(len(queue))
    elif k[0] == "pop":
        if len(queue) != 0 :
            print(queue.pop(0))
        else:
            print(-1)
    elif k[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

# collections library 굳이 안써도 stack 구조에 대한 이해
# pop() & pop(0),  insert(0,k[0]) & append(k[0]) 차이 이해