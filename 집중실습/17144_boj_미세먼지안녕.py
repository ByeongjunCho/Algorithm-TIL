from collections import deque
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for _ in range(T):
    # 미세먼지 확산
    airclean = []
    dust = []
    visit = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not arr[i][j]:
                continue
            elif arr[i][j] == -1:
                airclean.append([i, j])
            elif arr[i][j]:
                dust.append([i, j])
    Q = deque(dust)
    for _ in range(len(Q)):
        v = Q.popleft()
        for i in range(4):
            w = (v[0] + dx[i], v[1] + dy[i])
            if 0 <= w[0] < R and 0 <= w[1] < C and arr[w[0]][w[1]] != -1:
                Q.append(w)
                tmp = arr[v[0]][v[1]] // 5
                visit[v[0]][v[1]] -= tmp
                visit[w[0]][w[1]] += tmp
    for i in range(R):
        for j in range(C):
            arr[i][j] += visit[i][j]
            visit[i][j] = 0

    # 공기청정기 반시계
    s_row, s_col = airclean[0][0], airclean[0][1]
    s_row -= 1
    arr[s_row][s_col] = 0

    for i in range(s_row, 0, -1):  
        arr[i][0] = arr[i-1][0]
    for j in range(C-1):
        arr[0][j] = arr[0][j+1]
    for i in range(s_row+1):
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 1, -1):
        arr[s_row+1][j] = arr[s_row+1][j-1]
    arr[s_row+1][1] = 0

    # 공기청정기 시계
    s_row, s_col = airclean[1][0], airclean[1][1]
    s_row += 1
    arr[s_row][s_col] = 0
    
    for i in range(s_row, R-1):  
        arr[i][0] = arr[i+1][0]
    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, s_row-1, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 1, -1):
        arr[s_row-1][j] = arr[s_row-1][j-1]
    arr[s_row-1][1] = 0

result = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != -1:
            result += arr[i][j]
print(result)