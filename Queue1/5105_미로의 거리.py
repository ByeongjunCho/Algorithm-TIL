# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
from collections import deque

def BFS(v):
    status = [[-1,0], [1, 0], [0, 1], [0, -1]]
    Q = deque()
    Q.append(v)
    visit[v[0]][v[1]] = True
    P[v[0]][v[1]] = 1
    while Q:
        v = Q.popleft()
        for s in status:
            w = [v[0] + s[0], v[1] + s[1]]
            if 0 <= w[0] < len(arr) and 0 <= w[1] < len(arr) and not visit[w[0]][w[1]] and arr[w[0]][w[1]] != 1:
                Q.append(w)
                visit[w[0]][w[1]] = True
                D[w[0]][w[1]] = D[v[0]][v[1]] + 1
                P[w[0]][w[1]] = v
                if arr[w[0]][w[1]] == 3:
                    return D[w[0]][w[1]]-1
    return 0



T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    D = [[False for _ in range(N)] for _ in range(N)]  # 출발지점에서의 거리
    P = [[False for _ in range(N)] for _ in range(N)]  # 출발한 인덱스
    # 출발지점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                break
    print('#{} {}'.format(tc, BFS(start)))
