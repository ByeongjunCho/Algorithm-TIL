row = []
col = []
dp = [[-1 for _ in range(N)] for _ in range(N)]
def matrix(start, end):
    if start == end:
        return 0
    if dp[start][end] != -1:
        return dp[start][end]

    MIN = 0xffffff
    for k in range(start, end):
        left = matrix(start, k)
        right = matrix(k+1, end)
        if MIN > left + right + row[start]*col[k]*col[end]:
            MIN = left + right + row[start]*col[k]*col[end]
    dp[start][end] = MIN
    return MIN

