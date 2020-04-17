from collections import deque
N, M = map(int, input().split())  # 행, 열
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def bfs(v):
    Q = deque()
    Q.append(v)
    visit[v[0]][v[1]] = 1
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = v[0] + dy[i], v[1] + dx[i]
            if 0 <= wy < N and 0 <= wx < M and not visit[wy][wx] and arr[wy][wx]:
                Q.append((wy, wx))
                visit[wy][wx] = 1

def ice():
    tmp_arr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            tmp = 0
            for k in range(4):
                wy, wx = i + dy[k], j + dx[k]
                if 0 <= wy < N and 0 <= wx < M and arr[wy][wx] == 0:
                    tmp += 1
            tmp_arr[i][j] = tmp
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            if not tmp_arr[i][j]:
                continue
            arr[i][j] -= tmp_arr[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

            
result = 0
while True:
    ice()
    result += 1
    tmp = 0 # 빙산의 수
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and arr[i][j]:
                bfs((i, j))
                tmp += 1
    visit = [[0 for _ in range(M)] for _ in range(N)] # 방문기록 초기화
    
    if tmp == 0:
        print(0)
        break
    elif tmp > 1:
        print(result)
        break