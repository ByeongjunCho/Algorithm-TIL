from collections import deque
def bfs(order):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visit = [[0 for _ in range(5)] for _ in range(5)]
    start = order[-1]
    visit[start[0]][start[1]] = 1
    Q = deque()
    Q.append(start)
    cnt = 1
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = v[0] + dy[i], v[1] + dx[i]
            if (wy, wx) in order and not visit[wy][wx]:
                cnt += 1
                visit[wy][wx] = 1
                Q.append((wy, wx))
    if cnt != 7:
        return False
    else:
        return True

order = [(1,0), (1,1), (1,2), (1,3), (1,4), (2,1), (3,1)]
print(bfs(order))