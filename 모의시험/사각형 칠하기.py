
def draw_arr(idx1, idy1, idx2, idy2, xx):
    for row in range(idx1, idx2 + 1):
        for col in range(idy1, idy2 + 1):
            if DRAW[row][col] > xx:
                return
    for row in range(idx1, idx2 + 1):
        for col in range(idy1, idy2 + 1):
            if DRAW[row][col] < xx:
                DRAW[row][col] = xx
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N세로, M가로
    DRAW = [[0 for _ in range(M)] for _ in range(N)]

    status = [0]*11
    for _ in range(K):
        idx1, idy1, idx2, idy2, xx = map(int, input().split())
        draw_arr(idx1, idy1, idx2, idy2, xx)
    for i in range(N):
        for j in range(M):
            status[DRAW[i][j]] += 1
    # print(status)
    print('#{} {}'.format(tc, max(status)))






