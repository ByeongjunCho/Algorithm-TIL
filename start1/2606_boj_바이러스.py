
V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visit = [0] * (V+1)
def DFS(v):
    visit[v] = 1
    for w in G[v]:
        if not visit[w]:
            DFS(w)
DFS(1)
print(sum(visit)-1)