from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[v].append(u)


tmp = [0] * (N+1)
MAX = 0
for i in range(1, N+1):
    tmp_max = 0
    Q = deque()
    Q.append(i)
    visit[i] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = 1
                Q.append(w)
                tmp[i] += 1
                tmp_max += 1
    MAX = max(MAX, tmp_max)
    visit = [0 for _ in range(N + 1)]
result = []
for i in range(len(tmp)):
    if MAX == tmp[i]:
        result.append(i)
for i in range(len(result)):
    if i == len(result):
        print(result[i], end='')
    else:
        print(result[i], end=' ')
