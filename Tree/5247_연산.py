from collections import deque
def calc(s, e):
    MAX = 1000001

    dp = [0 for _ in range(MAX)]
    dp[s] = 0
    Q = deque()
    Q.append(s)

    while True:
        i = Q.popleft()
        if 0 <= i+1 < MAX and not dp[i+1]:
            dp[i+1] = dp[i]+1
            Q.append(i+1)
        if 0 <= i - 1 < MAX and not dp[i-1]:
            dp[i-1] = dp[i]+1
            Q.append(i-1)
        if 0 <= 2*i < MAX and not dp[i*2]:
            dp[i*2] = dp[i]+1
            Q.append(i*2)
        if 0 <= i-10 < MAX and not dp[i-10]:
            dp[i-10] = dp[i]+1
            Q.append(i - 10)
        if dp[e]:
            return dp[e]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, calc(N, M)))