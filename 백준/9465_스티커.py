T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(3)] for _ in range(n+1)]

    for i in range(n):
        dp[i+1][0] = max(dp[i][0], dp[i][1], dp[i][2])
        dp[i+1][1] = max(dp[i][0], dp[i][2]) + sticker[0][i]
        dp[i+1][2] = max(dp[i][0], dp[i][1]) + sticker[1][i]

    print(max(dp[n][0], dp[n][1], dp[n][2]))