from collections import deque
N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for g in G:
    if len(g) > 1:
        g.sort()
visit = [0 for _ in range(N+1)]

dfs_result = [str(V)]
def DFS(v):
    visit[v] = 1
    for w in G[v]:
        if not visit[w]:
            dfs_result.append(str(w))
            DFS(w)

bfs_result = [str(V)]
def BFS(v):

    Q = deque()
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
                bfs_result.append(str(w))

DFS(V)
visit = [0 for _ in range(N+1)]
BFS(V)
print(' '.join(dfs_result))
print(' '.join(bfs_result))