from queue import PriorityQueue
for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visit = [[False for _ in range(N)] for _ in range(N)]
    D = [[0xffffff for _ in range(N)] for _ in range(N)]
    P = [[0 for _ in range(N)] for _ in range(N)]

    D[0][0] = 0
    cnt = N*N - 1
    Q = PriorityQueue()
    Q.put((0, 0, 0))

    while not Q.empty():
        d, y, x = Q.get()
        if d > D[y][x]: continue


        # u, MIN = 0, 0xffffff
        # for i in range(N):
        #     for j in range(N):
        #         if not visit[i][j] and D[i][j] < MIN:
        #             u = (i, j)
        #             MIN = D[i][j]

        visit[y][x] = 1

        dy = (0, 0, 1, -1)
        dx = (1, -1, 0, 0)

        # dy = (0, 1)
        # dx = (1, 0)
        for i in range(4):
            wy, wx = y + dy[i], x + dx[i]
            if 0 <= wy < N and 0 <= wx < N and not visit[wy][wx]:
                weight = arr[wy][wx] - arr[y][x]
                weight = weight if weight > 0 else 0
                if D[wy][wx] > D[y][x] + weight + 1:
                    D[wy][wx] = D[y][x] + weight + 1
                    P[wy][wx] = (y, x)
                    Q.put((D[wy][wx], wy, wx))

    print('#{} {}'.format(tc, D[N-1][N-1]))


# # dp구현
# for tc in range(1, 1 + int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # dy = (0, 1)
#     # dx = (1, 0)
#     dy = (0, 0, 1, -1)
#     dx = (1, -1, 0, 0)
#
#     dp = [[0xffffff for _ in range(N)] for _ in range(N)]
#     dp[0][0] = 0
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 wy, wx = i + dy[k], j + dx[k]
#                 if 0 <= wy < N and 0 <= wx < N:
#                     weight = arr[wy][wx] - arr[i][j] if arr[wy][wx] - arr[i][j] > 0 else 0
#                     dp[wy][wx] = min(dp[wy][wx], dp[i][j] + weight + 1)
#     for d in dp:
#         print(d)
#     print('#{} {}'.format(tc, dp[N - 1][N - 1]))