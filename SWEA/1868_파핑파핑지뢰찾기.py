# 1868. 파핑파핑 지뢰찾기
from collections import deque
dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 위부터 시계방향으로
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(s):
    visit[s[0]][s[1]] = 1
    Q = deque()
    Q.append(s)
    while Q:
        v = Q.popleft()

        for i in range(8):
            wy, wx = dy[i] + v[0], dx[i] + v[1]
            # 주변에 폭탄이 하나라도 존재하면
            if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == '*' and not visit[wy][wx]:
                break
        else:
            for j in range(8):
                zy, zx = dy[j] + v[0], dx[j] + v[1]
                if 0 <= zy < N and 0 <= zx < N and not visit[zy][zx]:
                    visit[zy][zx] = 1
                    Q.append((zy, zx))

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            for k in range(8):
                wy, wx = dy[k] + i, dx[k] + j
                # 주변에 폭탄이 하나라도 존재하면 bfs를 수행하지 않음
                if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == '*' and not visit[wy][wx]:
                    break
            else:
                if not visit[i][j] and arr[i][j] !='*':
                    bfs((i, j))
                    count += 1
    # 남은 부분 수행
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and arr[i][j] !='*':
                # bfs((i, j))
                count += 1


    print('#{} {}'.format(tc, count))
