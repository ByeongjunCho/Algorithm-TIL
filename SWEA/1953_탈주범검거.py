# 1953. [모의 SW 역량테스트] 탈주범 검거
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

cy = []
def bfs(r, c):
    visit = [[0 for _ in range(M)] for _ in range(N)]

    Q = deque()
    Q.append((r, c))
    visit[r][c] = 1
    D[r][c] = 1
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 1:
            # 위로 가는 경우
            if 0 <= y - 1 < N and arr[y - 1][x] not in [0, 3, 4, 7] and not D[y - 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y-1][x] = D[y][x] + 1
                Q.append((y-1, x))
            # 오른쪽
            if 0 <= x + 1 < M and arr[y][x + 1] not in [0, 2, 4, 5] and not D[y][x + 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x+1] = D[y][x] + 1
                Q.append((y, x+1))
            # 아래
            if 0 <= y + 1 < N and arr[y + 1][x] not in [0, 3, 5, 6] and not D[y + 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y+1][x] = D[y][x] + 1
                Q.append((y+1, x))
            # 왼쪽
            if 0 <= x - 1 < M and arr[y][x - 1] not in [0, 2, 6, 7] and not D[y][x - 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x-1] = D[y][x] + 1
                Q.append((y, x-1))
        elif arr[y][x] == 2:
            # 위로 가는 경우
            if 0 <= y - 1 < N and arr[y - 1][x] not in [0, 3, 4, 7] and not D[y - 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y - 1][x] = D[y][x] + 1
                Q.append((y - 1, x))
            # 아래
            if 0 <= y + 1 < N and arr[y + 1][x] not in [0, 3, 5, 6] and not D[y + 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y + 1][x] = D[y][x] + 1
                Q.append((y + 1, x))

        elif arr[y][x] == 3:
            # 오른쪽
            if 0 <= x + 1 < M and arr[y][x + 1] not in [0, 2, 4, 5] and not D[y][x + 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x + 1] = D[y][x] + 1
                Q.append((y, x + 1))
            # 왼쪽
            if 0 <= x - 1 < M and arr[y][x - 1] not in [0, 2, 6, 7] and not D[y][x - 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x - 1] = D[y][x] + 1
                Q.append((y, x - 1))
        elif arr[y][x] == 4:
            # 위로 가는 경우
            if 0 <= y - 1 < N and arr[y - 1][x] not in [0, 3, 4, 7] and not D[y - 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y - 1][x] = D[y][x] + 1
                Q.append((y - 1, x))
            # 오른쪽
            if 0 <= x + 1 < M and arr[y][x + 1] not in [0, 2, 4, 5] and not D[y][x + 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x + 1] = D[y][x] + 1
                Q.append((y, x + 1))
        elif arr[y][x] == 5:
            # 오른쪽
            if 0 <= x + 1 < M and arr[y][x + 1] not in [0, 2, 4, 5] and not D[y][x + 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x + 1] = D[y][x] + 1
                Q.append((y, x + 1))
            # 아래
            if 0 <= y + 1 < N and arr[y + 1][x] not in [0, 3, 5, 6] and not D[y + 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y + 1][x] = D[y][x] + 1
                Q.append((y + 1, x))
        elif arr[y][x] == 6:
            # 아래
            if 0 <= y + 1 < N and arr[y + 1][x] not in [0, 3, 5, 6] and not D[y + 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y + 1][x] = D[y][x] + 1
                Q.append((y + 1, x))
            # 왼쪽
            if 0 <= x - 1 < M and arr[y][x - 1] not in [0, 2, 6, 7] and not D[y][x - 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x - 1] = D[y][x] + 1
                Q.append((y, x - 1))
        elif arr[y][x] == 7:
            # 위로 가는 경우
            if 0 <= y - 1 < N and arr[y - 1][x] not in [0, 3, 4, 7] and not D[y - 1][x]:
                if D[y][x] + 1 > L:
                    return
                D[y - 1][x] = D[y][x] + 1
                Q.append((y - 1, x))
            # 왼쪽
            if 0 <= x - 1 < M and arr[y][x - 1] not in [0, 2, 6, 7] and not D[y][x - 1]:
                if D[y][x] + 1 > L:
                    return
                D[y][x - 1] = D[y][x] + 1
                Q.append((y, x - 1))


def dfs(k, r, c):
    if k == L:
        return
    D[r][c] = 1
    if arr[r][c] == 1:
        # 위로 가는 경우
        if 0 <= r-1 < N and arr[r-1][c] not in [0, 3, 4, 7] and not D[r-1][c]:
            dfs(k+1, r-1, c)

        # 오른쪽
        if 0 <= c+1 < M and arr[r][c+1] not in [0, 2,4,5] and not D[r][c+1]:
            dfs(k+1, r, c+1)
        # 아래
        if 0 <= r+1 < N and arr[r+1][c] not in [0, 3,5,6] and not D[r+1][c]:
            dfs(k+1, r+1, c)
        # 왼쪽
        if 0 <= c-1 < M and arr[r][c-1] not in [0,2,6, 7] and not D[r][c-1]:
            dfs(k+1, r, c-1)
    elif arr[r][c] == 2:
        # 위로 가는 경우
        if 0 <= r - 1 < N and arr[r - 1][c] not in [0,3, 4, 7] and not D[r-1][c]:
            dfs(k + 1, r - 1, c)
        # 아래
        if 0 <= r+1 < N and arr[r+1][c] not in [0,3,5,6] and not D[r+1][c]:
            dfs(k+1, r+1, c)

    elif arr[r][c] == 3:
        # 오른쪽
        if 0 <= c + 1 < M and arr[r][c + 1] not in [0,2, 4, 5] and not D[r][c+1]:
            dfs(k + 1, r, c + 1)
        # 왼쪽
        if 0 <= c - 1 < M and arr[r][c - 1] not in [0,2, 6, 7] and not D[r][c-1]:
            dfs(k + 1, r, c - 1)
    elif arr[r][c] == 4:
        # 위로 가는 경우
        if 0 <= r - 1 < N and arr[r - 1][c] not in [0,3, 4, 7] and not D[r-1][c]:
            dfs(k + 1, r - 1, c)
        # 오른쪽
        if 0 <= c + 1 < M and arr[r][c + 1] not in [0,2, 4, 5] and not D[r][c+1]:
            dfs(k + 1, r, c + 1)
    elif arr[r][c] == 5:
        # 오른쪽
        if 0 <= c + 1 < M and arr[r][c + 1] not in [0,2, 4, 5] and not D[r][c+1]:
            dfs(k + 1, r, c + 1)
        # 아래
        if 0 <= r + 1 < N and arr[r + 1][c] not in [0,3, 5, 6] and not D[r+1][c]:
            dfs(k + 1, r + 1, c)
    elif arr[r][c] == 6:
        # 아래
        if 0 <= r + 1 < N and arr[r + 1][c] not in [0,3, 5, 6] and not D[r+1][c]:
            dfs(k + 1, r + 1, c)
        # 왼쪽
        if 0 <= c - 1 < M and arr[r][c - 1] not in [0,2, 6, 7] and not D[r][c-1]:
            dfs(k + 1, r, c - 1)
    elif arr[r][c] == 7:
        # 위로 가는 경우
        if 0 <= r - 1 < N and arr[r - 1][c] not in [3, 4, 7,0] and not D[r-1][c]:
            dfs(k + 1, r - 1, c)
        # 왼쪽
        if 0 <= c - 1 < M and arr[r][c - 1] not in [2, 6, 7,0] and not D[r][c-1]:
            dfs(k + 1, r, c - 1)

for tc in range(1, 1+int(input())):
    # 터널 세로, 가로 뚜껑 row, col, 탈출 시간 L
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[0 for _ in range(M)] for _ in range(N)]
    bfs(R, C)
    count = 0
    for i in range(N):
        for j in range(M):
            if D[i][j]:
                count += 1
    print('#{} {}'.format(tc, count))