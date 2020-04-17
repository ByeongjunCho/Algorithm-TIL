N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

S = set()
result = 0
def DFS(v):
    visit[v[0]][v[1]] = 1
    S.add(v)

    for w in union[v[0]][v[1]]:
        if not visit[w[0]][w[1]]:
            DFS(w)

while True:
    # 연합
    flag = 0
    union = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j < N-1:
                if L <= abs(arr[i][j] - arr[i][j+1]) <= R:
                    flag = 1
                    union[i][j].append((i, j+1))
                    union[i][j+1].append((i, j))
            if i < N-1:
                if L <= abs(arr[i][j] - arr[i + 1][j]) <= R:
                    flag = 1
                    union[i][j].append((i + 1, j))
                    union[i + 1][j].append((i, j))

    if not flag:
        break
    result += 1
    visit = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            DFS((i, j))
            if len(S) > 1:
                union_num = len(S)
                people = 0
                for a, b in S:
                    people += arr[a][b]
                tmp_people = people // union_num

                for a, b in S:
                    arr[a][b] = tmp_people
            S = set()

print(result)