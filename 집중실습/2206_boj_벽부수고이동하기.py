from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
D = [[0 for _ in range(M)] for _ in range(N)]

def BFS(v):
    visit[v[0]][v[1]] = 1
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    Q = deque()
    Q.append(v)
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = v[0] + dy[i], v[1] + dx[i]
            if 0 <= wy < N and 0 <= wx < M and not visit[wy][wx] and not arr[wy][wx]:
                Q.append([wy, wx])
                D[wy][wx] = D[v[0]][v[1]] + 1
                visit[wy][wx] = 1

result = 0xffff

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            arr[i][j] = 0
            BFS([0, 0])
            if D[N-1][M-1]:
                result = min(result, D[N-1][M-1])
            visit = [[0 for _ in range(M)] for _ in range(N)]
            D = [[0 for _ in range(M)] for _ in range(N)]
            arr[i][j] = 1

# 벽을 부수지 않는 경우
BFS([0, 0])
if D[N - 1][M - 1]:
    result = min(result, D[N - 1][M - 1])

if result == 0xffff:
    print(-1)
else:
    print(result+1)