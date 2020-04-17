result = 0xffff
def perm(k, n):
    if k == n:
        tmp = 0
        i = 0
        while i < len(order) - 1:
            tmp += arr[order[i]][order[i + 1]]
            i += 1
        tmp += arr[0][order[0]]
        tmp += arr[order[-1]][0]
        global result
        result = min(result, tmp)
        return

    for i in range(k, n):
        order[k], order[i] = order[i], order[k]
        perm(k+1, n)
        order[i], order[k] = order[k], order[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = list(range(1, N))
    perm(0, N-1)
    print('#{} {}'.format(tc, result))
    result = 0xffff

