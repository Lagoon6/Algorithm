# 1,2,3 더하기
# recursive 생각하기
import sys

T = int(sys.stdin.readline())
result = []
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dp(n-1) + dp(n-2) + dp(n-3)
# f(n) = f(n-1) + f(n-2) + f(n-3)
# 1, 2, 4, 7, 13
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp(n))
