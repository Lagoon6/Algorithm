# 1676 #S4
#  정수론
import sys

N = int(sys.stdin.readline())

cnt = 0
while N >= 5:
    cnt += N//5
    N //= 5
    
print(cnt)
# 10! -> 2
# 5! -> 1
# 15! ->3
