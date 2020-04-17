N, M = map(int, input().split())
visit = [[0 for _ in range(M)] for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# 0: 북쪽    1: 동쪽    2: 남쪽    3: 서쪽
r_y, r_x, mode = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
def clean(y, x, mode):
    visit[y][x] = 1
    # 2.a
    tmp_mode = mode - 1
    if tmp_mode < 0:
        tmp_mode = 3
    wy, wx = y + dy[tmp_mode], x + dx[tmp_mode]
    if 0 <= wy < N and 0<=wx< M and not arr[wy][wx] and not visit[wy][wx]:
        clean(wy, wx, tmp_mode)

    flag = 0
    for i in range(4):
        wy, wx = y + dy[i], x + dx[i]
        if 0 > wy or wy > N - 1 or 0 > wx or wx > M - 1:
            flag += 1
        elif 0 <= wy < N and 0 <= wx < M or arr[wy][wx] or visit[wy][wx]:
            flag += 1
    if flag == 4:
        if 0 <= y - dy[tmp_mode] < N and 0 <= x - dx[tmp_mode] < M and not visit[y-dy[tmp_mode]][x-dx[tmp_mode]] and not arr[y-dy[tmp_mode]][x-dx[tmp_mode]]:
            clean(y - dy[tmp_mode], x - dx[tmp_mode], mode)
        else:
            return
    else:
        wy, wx = y + dy[tmp_mode], x + dx[tmp_mode]
        if visit[wy][wx] or arr[wy][wx]: # 0 <= wy < N and 0 <= wx < M or
            clean(y, x, tmp_mode)

clean(r_y, r_x, mode)
result = 0
for i in range(N):
    for j in range(M):
        result += visit[i][j]
# print(visit)
print(result)
