from collections import deque
N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visit = [0 for _ in range(N+1)]

def BFS(v):
    Q = deque([v])
    visit[v] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = 1
                Q.append(w)

# def DFS(v):
#     visit[v] = 1
#     for w in G[v]:
#         if not visit[w]:
#             DFS(w)

result = 0
for i in range(1, N+1):
    if not visit[i]:
        result += 1
        BFS(i)
print(result)