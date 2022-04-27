from collections import deque
class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

G1 = None
stack = []
visitedAry = []

gSize = 6
G1 = Graph(gSize)
G1.graph[0 ][1] = 1;G1.graph[0][2] = 1
G1.graph[1][0] = 1;G1.graph[1][3] = 1
G1.graph[2][0] = 1;G1.graph[2][3] = 1
G1.graph[3][1] = 1;G1.graph[3][2] = 1;G1.graph[3][4] =1; G1.graph[3][5] = 1
G1.graph[4][3] = 1;G1.graph[4][5] = 1
G1.graph[5][3] = 1;G1.graph[5][4] = 1

current = 0
stack.append(current)
visitedAry.append(current)

while(len(stack) !=0):
    next = None
    for vertex in range(gSize):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex


    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문순서-->', end ="")
for i in visitedAry:
    print(i, end="")
            
