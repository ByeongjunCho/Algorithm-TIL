from collections import deque
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

count = 0

while True:
    signal = 1
    for i in range(N):
        for j in range(N):
            # BFS
            if not visit[i][j]:
                Q = deque()
                Q.append((i, j))
                # union = [(i, j)]
                union = []
                SUM = arr[i][j]
                while Q:
                    v = Q.popleft()
                    union.append(v)
                    visit[v[0]][v[1]] = 1
                    for k in range(4):
                        wy, wx = v[0] + dy[k], v[1] + dx[k]
                        if 0 <= wy < N and 0 <= wx < N and not visit[wy][wx]:
                            if L <= abs(arr[wy][wx] - arr[v[0]][v[1]]) <= R:
                                Q.append((wy, wx))
                                visit[wy][wx] = 1
                                SUM += arr[wy][wx]
                union = set(union)
                people = int(SUM/len(union))

                for row, col in union:
                    if arr[row][col] != people:
                        arr[row][col] = people
                        signal = 2
    if signal == 1:
        break
    else:
        count += 1
    visit = [[0 for _ in range(N)] for _ in range(N)]
print(count)