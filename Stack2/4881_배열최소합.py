# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합


def perm(k, n, used, arr_sum):
    if arr_sum > result[-1]:
        return
    if k == n:
        result[-1] = arr_sum
        return

    for i in range(n):
        if used & (1 << i):
            continue
        order[k] = i
        perm(k+1, n, used | (1 << i), arr_sum + arr[k][i])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = [0] * N
    result = [90]
    perm(0, N, 0, 0)
    print('#{} {}'.format(tc, result[-1]))
    result = [90]