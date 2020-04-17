N, M = map(int, input().split()) # 행, 열
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
yx_cond = [] # 좌표 후보군
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            yx_cond.append((i, j))

def dfs(v):
    visit[v[0]][v[1]] = 1
    for i in range(4):
        wy, wx = v[0] + dy[i], v[1] + dx[i]
        if 0<=wy<N and 0<=wx<M and arr[wy][wx] != 1 and not visit[wy][wx]:
            dfs((wy, wx))

result = 0

for i in range(len(yx_cond)):
    arr[yx_cond[i][0]][yx_cond[i][1]] = 1
    for j in range(i+1, len(yx_cond)):
        arr[yx_cond[j][0]][yx_cond[j][1]] = 1
        for k in range(j+1, len(yx_cond)):
            arr[yx_cond[k][0]][yx_cond[k][1]] = 1
            for r in range(N):
                for c in range(M):
                    if arr[r][c] == 2 and not visit[r][c]:
                        dfs((r,c))
            cnt = 0
            for r in range(N):
                for c in range(M):
                    if arr[r][c] == 0 and visit[r][c] == 0:
                        cnt += 1
            result = max(result, cnt)
            
            visit = [[0 for _ in range(M)] for _ in range(N)]
            arr[yx_cond[k][0]][yx_cond[k][1]] = 0
        arr[yx_cond[j][0]][yx_cond[j][1]] = 0
    arr[yx_cond[i][0]][yx_cond[i][1]] = 0
print(result)