# BFS로 풀이

from collections import deque
n = int(input())
G = [[] for _ in range(n+1)]
D = [0 for _ in range(n+1)]

tar1, tar2 = map(int, input().split())


for _ in range(int(input())):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

Q = deque()
Q.append(tar1)
D[tar1] = 1
while Q:
    w = Q.popleft()
    for v in G[w]:
        if not D[v]:
            Q.append(v)
            D[v] = D[w] + 1
    if D[tar2]:
        break
print(D[tar2]-1)