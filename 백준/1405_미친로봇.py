arr = list(map(int, input().split()))
visit = [[0 for _ in range(40)] for _ in range(40)]
result = 0
# ewsn = arr[1:]  # 동서남북
dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]

def dfs(k, v, vals):
    if vals == 0:
        return
    if k == arr[0]:
        global result
        result += vals
        return
    visit[v[0]][v[1]] = 1
    for i in range(1, 5):
        wy, wx = v[0] + dy[i], v[1] + dx[i]
        if not visit[wy][wx]:
            dfs(k+1, (wy, wx), vals * arr[i]*0.01)
            visit[wy][wx] = 0

dfs(0, (20, 20), 1)
print('{:.9f}'.format(result))