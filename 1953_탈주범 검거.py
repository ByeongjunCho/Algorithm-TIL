# 1953. [모의 SW 역량테스트] 탈주범 검거

from collections import deque
t0 = []
t1 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
t2 = [[1, 0], [-1, 0]]
t3 = [[0, 1], [0, -1]]
t4 = [[-1, 0], [0, 1]]
t5 = [[1, 0], [0, 1]]
t6 = [[1, 0], [0, -1]]
t7 = [[-1, 0], [0, -1]]

stats = {x: eval("t"+str(x)) for x in range(8)}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split()) # 하수구 높이, 너비, 뚜껑위치RC, 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    """BFS 구현"""
    # bfsd = [[0xffff for _ in range(M)] for _ in range(N)]
    # def bfs(r, c):
    #     bfsd[r][c] = 1
    #     Q = deque()
    #     Q.append((r, c))
    #     while Q:
    #         y, x = Q.popleft()
    #         for dy, dx in stats.get(arr[y][x]):
    #             wy, wx = y + dy, x + dx
    #             if 0 <= wy < N and 0 <= wx < M and [-dy, -dx] in stats.get(arr[wy][wx]) and bfsd[wy][wx] > bfsd[y][x] + 1 and bfsd[y][x] + 1 <= L:
    #                 bfsd[wy][wx] = bfsd[y][x] + 1
    #                 Q.append((wy, wx))
    # bfs(R, C)
    # cnt = 0
    # for i in range(N):
    #     for j in range(M):
    #         if bfsd[i][j] <= L:
    #             cnt += 1

    """DFS구현"""
    dfsd = [[0 for _ in range(M)] for _ in range(N)]
    def dfs(y, x, cnt):
        dfsd[y][x] = cnt
        for dy, dx in stats.get(arr[y][x]):
            wy, wx = y + dy, x + dx
            if 0 <= wy < N and 0 <= wx < M and [-dy, -dx] in stats.get(arr[wy][wx]) and cnt <= L:
                if not dfsd[wy][wx]:
                    dfs(wy, wx, cnt+1)
                elif dfsd[wy][wx] > cnt+1:
                    dfs(wy, wx, cnt+1)

    dfs(R, C, 1)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < dfsd[i][j] <= L:
                cnt += 1
    print("#{} {}".format(tc, cnt))