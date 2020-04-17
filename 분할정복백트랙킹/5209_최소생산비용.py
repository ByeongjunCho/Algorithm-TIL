T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1500
    def perm(k, used, vals):
        global result
        if vals > result:
            return
        if k == N:

            result = min(result, vals)

        for i in range(N):
            if used & (1 << i):
                continue
            perm(k+1, used | (1 << i), vals + arr[k][i])
    perm(0, 0, 0)
    print('#{} {}'.format(tc, result))
