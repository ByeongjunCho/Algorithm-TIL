from collections import deque
h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
D = [[0 for _ in range(w)] for _ in range(h)]

def BFS(v):
    dy = (0, 0, 1, -1)
    dx = (1, -1, 0, 0)
    Q = deque()
    Q.append(v)
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = v[0] + dy[i], v[1] + dx[i]
            if 0 <= wy < h and 0 <= wx < w and arr[wy][wx] == 'L' and not D[wy][wx]:
                D[wy][wx] = D[v[0]][v[1]] + 1
                Q.append((wy, wx))

result = 0
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L' and not D[i][j]:
            BFS((i, j))
            for vals in D:
                result = max(result, max(vals))
            D = [[0 for _ in range(w)] for _ in range(h)]

print(result)