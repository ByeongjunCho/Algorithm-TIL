# def f(n):
#     if n == 1:
#         return 0
#     if dp[n]:
#         return dp[n]
#     result = f(n-1) + 1
#     if n%3 == 0:
#         result = min(result, f(n//3) + 1)
#     if n%2 == 0:
#         result = min(result, f(n // 2) + 1)
#     dp[n] = result
#     return dp[n]

def f(N):
    for i in range(1, N):
        dp[i+1] = min(dp[i+1], dp[i] + 1)
        if 2*i < len(dp):
            dp[2*i] = min(dp[2*i], dp[i] + 1)
        if 3*i < len(dp):
            dp[3*i] = min(dp[3*i], dp[i] + 1)
    return dp[N]


N = int(input())
dp = [1000001] * (N+1)
dp[1] = 0
print(f(N))