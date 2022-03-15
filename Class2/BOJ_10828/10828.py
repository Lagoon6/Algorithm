#SILVER 4 
#Stack

import sys

N = int(sys.stdin.readline())


stack = []
for _ in range(N):
    k = sys.stdin.readline().split()
    if k[0] == "push":
        stack.append(k[1])
    elif k[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif k[0] == "size":
        print(len(stack))
    elif k[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)    
    elif k[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])

# 10845와 동일