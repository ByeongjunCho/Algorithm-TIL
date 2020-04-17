# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    D = [0 for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, end = map(int, input().split())

    Q = deque()
    Q.append(start)
    visit[start] = True
    result = 0
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = True
                D[w] = D[v] + 1
                if w == end:
                    result = D[w]
                    Q = []
                    break
    print('#{} {}'.format(tc, result))