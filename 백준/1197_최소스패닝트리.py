# boj-1197 최소 스패닝 트리
## prim 알고리즘
# from queue import PriorityQueue
# V, E = map(int, input().split())
# G = [[] for _ in range(V + 1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     G[u].append([v, w])
#     G[v].append([u, w])
#
#
# visit = [0] * (V+1)
# key = [0xffffffffff] * (V+1)
#
# visit[1] = 1
# key[1] = 0
# Q = PriorityQueue()
# Q.put((0, 1))
#
#
# while not Q.empty():
#     w, v = Q.get()
#     visit[v] = 1
#
#     for node, weight in G[v]:
#         if key[node] > weight and not visit[node]:
#             key[node] = weight
#             Q.put((weight, node))
#
# result = 0
# for i in range(V+1):
#     if key[i] < 0xffffffffff:
#         result += key[i]
# print(result)

# 크루스칼 알고리즘
from queue import PriorityQueue
V, E = map(int, input().split())

q = PriorityQueue()
Edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    Edge.append((w, u, v))
    # q.put((w, u, v))

p = [x for x in range(V+1)]

def findset(x):
    if p[x] != x:
        p[x] = findset(p[x])
    return p[x]


cnt = V-1
idx = 0
result = 0
Edge.sort()
while cnt:
    w, u, v = Edge[idx]
    # w, u, v = q.get()
    a = findset(u)
    b = findset(v)

    if a != b:
        p[b] = a
        result += w
        cnt -= 1
    idx += 1
print(result)