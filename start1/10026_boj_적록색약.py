from collections import deque
N = int(input())
arr = [input() for _ in range(N)]

visit = [[0 for _ in range(N)] for _ in range(N)]
status = [0] * 3  # RGB

def BFS(start):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    Q = deque()
    Q.append(start)
    visit[start[0]][start[1]] = 1
    mode = arr[start[0]][start[1]]
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = dy[i] + v[0], dx[i] + v[1]
            if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == mode and not visit[wy][wx]:
                visit[wy][wx] = 1
                Q.append((wy, wx))
