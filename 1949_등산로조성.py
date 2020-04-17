# 1949. [모의 SW 역량테스트] 등산로 조성


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = []
    top = 0
    maxLen = 0  # 가장 긴 등산로 길이
    # 가장 높은 봉우리를 구함
    for _ in range(N):
        tmp = list(map(int, input().split()))
        top = max(max(tmp), top)
        board.append(tmp)

    # dfs구현
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    def dfs(y, x, dig, length):  # 행, 렬, 등산로 제거 상태, 길이
        global maxLen
        maxLen = max(maxLen, length)
        visit[y][x] = 1
        for i in range(4):
            wy, wx = y + dy[i], x + dx[i]
            if 0 <= wy < N and 0 <= wx < N and not visit[wy][wx]:
                if board[wy][wx] >= board[y][x] and not dig and board[wy][wx] - K < board[y][x]:
                    temp = board[wy][wx]
                    board[wy][wx] = board[y][x] - 1
                    dfs(wy, wx, 1, length+1)
                    board[wy][wx] = temp
                elif board[wy][wx] < board[y][x]:
                    dfs(wy, wx, dig, length+1)
        visit[y][x] = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == top:
                visit = [[0 for _ in range(N)] for _ in range(N)]
                dfs(i, j, 0, 1)

    print("#{} {}".format(tc, maxLen))