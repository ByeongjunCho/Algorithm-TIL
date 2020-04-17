result = 0
arr_xy = [0] * 25
k = 0
# 모든 좌표를 벡터로 변형
for i in range(5):
    for j in range(5):
        arr_xy[k] = (i,j)  # 모든 좌표의 경우의 수
        k += 1
# 근접 행렬인지 판단
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


order = []
def comb(k, start, y):
    if y > 3:
        return
    if len(order) == 7:
        if bfs(order):
            global result
            result += 1
        return

    for i in range(start, 25):
        if arr[arr_xy[i][0]][arr_xy[i][1]] == 'Y':
            order.append(arr_xy[i])
            comb(k+1, i+1, y+1)
            order.pop()
        else:
            order.append(arr_xy[i])
            comb(k+1, i+1, y)
            order.pop()

arr = [input() for _ in range(5)]
comb(0, 0, 0)
print(result)