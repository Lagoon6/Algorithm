#GOLD 5
# AC 문제
# 빈 배열 [] 출력 + 문자열 구현 생각하기
# 결과 -> list(deque)가 아닌 문자열로 출력하기 (빈칸 띄어쓰기 잘봐야함)
import sys
from collections import deque


T = int(sys.stdin.readline())

for _ in range(T):
    cmd = list(input())
    len_arr = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    num_list = deque(arr)
    cnt = 0
    tmp = 0
    if len_arr ==0:
        num_list = []
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            cnt +=1
        elif cmd[i] =='D': 
            if len(num_list) == 0:
                tmp = 1
                print("error")
                break
            else:
                if cnt % 2 ==0:
                    num_list.popleft()
                else:
                    num_list.pop()
    if tmp == 0:
        if cnt % 2 ==0:
            print("[" + ",".join(num_list) + "]")
        else:
            num_list.reverse()
            print("[" + ",".join(num_list) + "]")




''''
for _ in range(T):
    num_list = deque()
    cmd = list(input())
    len_arr = int(sys.stdin.readline())
    arr = sys.stdin.readline().split(',')
    for i in range(len_arr):
        if i == 0:
            num_list.append(arr[i][1])
        elif i == len_arr-1:
            num_list.append(arr[len_arr-1][0])
        else:
            num_list.append(arr[i])
        
    for i in range(len(cmd)):
        if len(num_list) ==0:
            print('error')
        else:
            if cmd[i] == 'R':
                num_list.reverse()
            elif cmd[i] =='D':
                num_list.popleft()
    print(list(num_list))
'''