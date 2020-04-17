def fact(n): # n=문제를 식별하는 값, 문제의 크기
    if n == 0 or n== 1:
        return 1
    return fact(n-1) * n

def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1) + fibo(n - 2)


memo = [-1] * 101
def fibo(n):
    if n==0 or n==1:
        return n
    if memo[n] != -1: # 답을 구함
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n - 2)
        return memo[n]

print(fibo(40))


# fibo memorization
# memo = [-1, -1, -1, -1, -1, -1, -1]
# fibo(7) 6 5 4 3 2 1 0
memo = [-1] * 101
def fibo(n):
    memo[0], memo[1] = 0, 1

    for i in range(2, n + 1):   # i-> 문제를 식별하는 값
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

