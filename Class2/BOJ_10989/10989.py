#class2
#메모리 절약 문제
#[0]*10,001 개의 최대 메모리 만들어놓고 -> 그 위치의 값에 +=1로 할당 구조 
import sys
N = int(sys.stdin.readline())
num_list = [0]*10001

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i in range(len(num_list)): 
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)