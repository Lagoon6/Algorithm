# SILVER 4
# queue

import sys
from collections import deque
N = int(sys.stdin.readline())

num_list = deque([i+1 for i in range(N)])

while len(num_list) > 1:
    num_list.popleft()
    num_list.append(num_list.popleft())
print(num_list[0])