# 연결 요소의 개수

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
print(G)