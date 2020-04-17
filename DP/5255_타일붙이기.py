dp = [0] * 31
dp[1] = 1
dp[2] = 3
dp[3] = 6
for i in range(4, 31):
    dp[i] = dp[i - 1] + 2 * dp[i - 2] + dp[i - 3]

for tc in range(1, 1 + int(input())):
    N = int(input())
    print('#{} {}'.format(tc, dp[N]))