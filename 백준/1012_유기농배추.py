from collections import deque
T = int(input())
for _ in range(T):
    M, N, T = map(int, input().split())  # 가로, 세로, 배추 위치의 개수
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(T):
        x, y = map(int, input().split())
        arr[y][x] = 1
    result = 0
    dy = (0, 0, 1, -1)
    dx = (1, -1, 0, 0)
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and arr[i][j]:
                result += 1
                Q = deque()
                Q.append((i, j))
                visit[i][j] = 1
                while Q:
                    v = Q.popleft()
                    for k in range(4):
                        wy, wx = v[0] + dy[k], v[1] + dx[k]
                        if 0 <= wy < N and 0 <= wx < M and arr[wy][wx] and not visit[wy][wx]:
                            Q.append((wy, wx))
                            visit[wy][wx] = 1
    print(result)