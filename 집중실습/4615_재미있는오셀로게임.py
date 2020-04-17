# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [[0 for _ in range(N)] for _ in range(N)]
#     half_N = N >> 1
#     arr[half_N-1][half_N-1], arr[half_N][half_N] = 2, 2
#     arr[half_N][half_N - 1], arr[half_N-1][half_N] = 1, 1
#
#     for _ in range(M):
#         y, x, color = map(int, input().split())
#         y = y-1
#         x = x-1
#         arr[x][y] = color
#         if color == 1:
#             # 우측 확인
#             if y + 2 < N and arr[x][y+1] == 2 and arr[x][y+2] == color:
#                 arr[x][y + 1] = 1
#             # 아래 확인
#             if x + 2 < N and arr[x+1][y] == 2 and arr[x+2][y] == color:
#                 arr[x + 1][y] = 1
#             # 왼쪽 확인
#             if y - 2 >= 0 and arr[x][y-1] == 2 and arr[x][y-2] == color:
#                 arr[x][y - 1] = 1
#             # 위 확인
#             if x - 2 >= 0 and arr[x - 1][y] == 2 and arr[x - 2][y] == color:
#                 arr[x - 1][y] = 1
#             # 오른쪽 위 대각선 확인
#             if x - 2>=0 and y+2 < N and arr[x-1][y+1] == 2 and arr[x-2][y+2] == color:
#                 arr[x-1][y+1] = 1
#             # 오른쪽 아래 대각선 확인
#             if x + 2 < N and y+2 < N and arr[x+1][y+1] == 2 and arr[x+2][y+2] == color:
#                 arr[x+1][y+1] = 1
#             # 왼쪽 아래 대각선 확인
#             if x + 2 < N and y-2 >= 0 and arr[x+1][y-1] == 2 and arr[x+2][y-2] == color:
#                 arr[x+1][y-1] = 1
#             # 왼쪽 위
#             if x - 2 >= 0 and y-2 >= 0 and arr[x-1][y-1] == 2 and arr[x-2][y-2] == color:
#                 arr[x-1][y-1] = 1
#         else:
#             # 우측 확인
#             if y + 2 < N and arr[x][y + 1] == 1 and arr[x][y + 2] == color:
#                 arr[x][y + 1] = 2
#             # 아래 확인
#             if x + 2 < N and arr[x + 1][y] == 1 and arr[x + 2][y] == color:
#                 arr[x + 1][y] = 2
#             # 왼쪽 확인
#             if y - 2 >= 0 and arr[x][y - 1] == 1 and arr[x][y - 2] == color:
#                 arr[x][y - 1] = 2
#             # 위 확인
#             if x - 2 >= 0 and arr[x - 1][y] == 1 and arr[x - 2][y] == color:
#                 arr[x - 1][y] = 2
#             # 오른쪽 위 대각선 확인
#             if x - 2 >= 0 and y + 2 < N and arr[x - 1][y + 1] == 1 and arr[x - 2][y + 2] == color:
#                 arr[x - 1][y + 1] = 2
#             # 오른쪽 아래 대각선 확인
#             if x + 2 < N and y + 2 < N and arr[x + 1][y + 1] == 1 and arr[x + 2][y + 2] == color:
#                 arr[x + 1][y + 1] = 2
#             # 왼쪽 아래 대각선 확인
#             if x + 2 < N and y - 2 >= 0 and arr[x + 1][y - 1] == 1 and arr[x + 2][y - 2] == color:
#                 arr[x + 1][y - 1] = 2
#             # 왼쪽 위
#             if x - 2 >= 0 and y - 2 >= 0 and arr[x - 1][y - 1] == 1 and arr[x - 2][y - 2] == color:
#                 arr[x - 1][y - 1] = 2
#
#     result = [0] * 2
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 result[0] += 1
#             elif arr[i][j] == 2:
#                 result[1] += 1
#
#     print('#{} {} {}'.format(tc, result[0], result[1]))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    half_N = N >> 1
    arr[half_N-1][half_N-1], arr[half_N][half_N] = 2, 2
    arr[half_N][half_N - 1], arr[half_N-1][half_N] = 1, 1

    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]

    for _ in range(M):
        x, y, color = map(int, input().split())
        y -= 1  # 행
        x -= 1  # 열
        arr[y][x] = color
        if color == 1:
            for i in range(8):
                y_n = y+dy[i]
                x_n = x+dx[i]
                if 0 <= y_n < N and 0 <= x_n < N and arr[y_n][x_n] == 2:
                    while 0 <= y_n < N and 0 <= x_n < N:
                        if arr[y_n][x_n] == 1:
                            while y+dy[i] != y_n or x+dx[i] != x_n:
                                y_n -= dy[i]
                                x_n -= dx[i]
                                arr[y_n][x_n] = 1
                            break
                        y_n += dy[i]
                        x_n += dx[i]
        else:
            for i in range(8):
                y_n = y+dy[i]
                x_n = x+dx[i]
                if 0 <= y_n < N and 0 <= x_n < N and arr[y_n][x_n] == 1:
                    while 0 <= y_n < N and 0 <= x_n < N:
                        if arr[y_n][x_n] == 2:
                            while y+dy[i] != y_n or x+dx[i] != x_n:
                                y_n -= dy[i]
                                x_n -= dx[i]
                                arr[y_n][x_n] = 2
                            break
                        y_n += dy[i]
                        x_n += dx[i]

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc, black, white))