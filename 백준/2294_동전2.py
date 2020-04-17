n, k = map(int, input().split())
MIN = 100001
coin = [0] * n
for i in range(n):
    coin[i] = int(input())
    MIN = min(coin[i], MIN)

dp = [[30 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    dp[i][0] = 0
    for j in range(k+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        jj = j + coin[i]
        if jj <= k:
            dp[i][jj] = min(dp[i][jj], dp[i][j] + 1)

if dp[n-1][k] == 100001:
    print(-1)
else:
    print(dp[n-1][k])