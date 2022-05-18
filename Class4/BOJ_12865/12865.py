

from abc import abstractproperty
import sys

def knapsak(maxWeight, rowCount, weight, money):
    #메모이제이션 배열
    array = [[ 0 for _ in range(maxWeight+1)] for _ in range(rowCount +1)]
    for row in range(1,rowCount+1):
        for col in range(1, maxWeight+1):
            if weight[row]> col:
                array[row][col] = array[row-1][col]
            else:
                value1 = money[row] + array[row-1][col-weight[row]]
                value2 = array[row-1][col]
                if value1 > value2:
                    array[row][col] = value1      
                else:
                    array[row][col] = value2
            print('%6d'%array[row][col], end = '')
        print()
    return array[rowCount][maxWeight]

N, M = map(int,sys.stdin.readline().split())
maxWeight = M
rowCount = N
weight = [0]
value = [0]   
for _ in range(N):
    W, V = map(int,sys.stdin.readline().split())
    weight.append(W)
    value.append(V)


knapsak(maxWeight, rowCount, weight, value)


####################################
import sys
N, K =map(int,sys.stdin.readline().split())
catch  ={0:0}

for _ in range(N):
    curr_w , curr_v = map(int,sys.stdin.readline().split())
    temp = {}
    for w,v in catch.items():
        if curr_w + w <= K and curr_v + v > catch.get(curr_w+w, 0):
            temp[curr_w+w] = curr_v+v
            print(temp)
    print(catch)
    catch.update(temp)
    print(catch)
print(catch)
# reference python code BOj #doju00