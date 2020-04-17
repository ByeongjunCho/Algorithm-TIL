def search_min(y, x, val, N):
    global result
    if val > result:
        return
    if y == N-1 and x == N-1:

        all_val = val + arr[y][x]
        result = min(result, all_val)
        return

    for i in range(2):
        wy, wx = y + dy[i], x + dx[i]
        if 0 <= wy < N and 0 <= wx < N:
            search_min(wy, wx, val+arr[y][x], N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0xffff
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = (0, 1)
    dx = (1, 0)
    search_min(0, 0, 0, N)
    print('#{} {}'.format(tc, result))
