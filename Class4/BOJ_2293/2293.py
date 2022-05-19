import sys

n, k = map(int,sys.stdin.readline().split())
coin_list = []
dp = [0 for _ in range(k+1)] # dp[0] ~ dp[10]
dp[0] = 1 # 처음 1개

for _ in range(n):
    c = int(sys.stdin.readline())
    coin_list.append(c)

# coin = 1, 2, 5
for coin in coin_list:
    for i in range(coin,len(dp)):
        if dp[i]*coin >= 0 :
            dp[i] = dp[i] + dp[i-coin]

print(dp[k])