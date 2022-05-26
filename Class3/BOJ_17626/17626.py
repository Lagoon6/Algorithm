import sys

n = sys.stdin.readline()
dp = [0]*(n+1)
dp[0], dp[1] = 0,1

for _ in range(n):
