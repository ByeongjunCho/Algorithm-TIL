def tomato():
    dy = (0, 0, -1, 1)
    dx = (1, -1, 0, 0)
    while target:
        v = target.pop()
        for i in range(4):
            wy, wx = v[1] + dy[i], v[2] + dx[i]
            if 0 <= wy < N and 0 <= wx < M and arr[v[0]][wy][wx] == 0:


M, N, H = map(int, input().split()) # 가로, 세로, 높이
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
target = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                target.append((i, j, k))
if len(target) == 0:
    print(0)
