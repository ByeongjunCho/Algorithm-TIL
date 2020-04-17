from collections import deque
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visits = [[0 for _ in range(N)] for _ in range(N)]

rain_max = 0
for i in range(N):
    for j in range(N):
        rain_max = max(rain_max, arr[i][j])

dy = (0,0,1,-1)
dx = (1,-1,0,0)

def bfs(v, rain):
    Q = deque()
    Q.append(v)
    visits[v[0]][v[1]] = 1
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = v[0] + dy[i], v[1] + dx[i]
            if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] > rain and not visits[wy][wx]:
                Q.append((wy, wx))
                visits[wy][wx] = 1

result = 0
for r in range(rain_max+1):
    tmp = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > r and not visits[i][j]:
                bfs((i, j), r)
                tmp += 1
    result = max(result, tmp)
    visits = [[0 for _ in range(N)] for _ in range(N)]

print(result)