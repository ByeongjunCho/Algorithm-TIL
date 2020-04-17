from collections import deque

def BFS(arr, N):
    status = [[-1, 0], [0, 1], [1, 0], [0,-1]]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i,j]
                break

    visit[start[0]][start[1]] = True
    Q = deque()
    Q.append(start)

    while Q:
        v = Q.popleft()
        for s in status:
            w = [s[0] + v[0], s[1] + v[1]]
            if 0 <= w[0] < N and 0 <= w[1] < N and arr[w[0]][w[1]] != 1 and not visit[w[0]][w[1]]:
                # if not visit[w[0]][w[1]]:
                visit[w[0]][w[1]] = True
                Q.append(w)
                D[w[0]][w[1]] = D[v[0]][v[1]] + 1
                P[w[0]][w[1]] = v
                if arr[w[0]][w[1]] == 3:
                    return 1, [w[0], w[1]]
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    D = [[0 for _ in range(N)] for _ in range(N)]  # 거리 탐색
    P = [[0 for _ in range(N)] for _ in range(N)]  # 방문 탐색
    # print('#{} {}'.format(tc, BFS(arr, N)))
    _, v = BFS(arr, N)
    print(v)
    S = [v]
    while v != [4,3] :
        i, j = v
        v = P[i][j]
        S.append(v)
    print(S[::-1])



