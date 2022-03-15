#SILVER 4 
#queue
import sys

N = int(sys.stdin.readline())

deque = []

for _ in range(N):
    k = list(sys.stdin.readline().split())

    if k[0] == "push_front":
        deque.insert(0,k[1])
    
    elif k[0] == "push_back":
        deque.append(k[1])
    
    elif k[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif k[0] =="pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])
            del deque[len(deque)-1]
    elif k[0] =="size":
        print(len(deque))
    
    elif k[0] =="empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif k[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif k[0] =="back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])