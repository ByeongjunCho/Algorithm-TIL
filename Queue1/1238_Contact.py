# 1238. [S/W 문제해결 기본] 10일차 - Contact
from collections import deque

for tc in range(1, 11):
    N, start = map(int, input().split())
    tmp = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    for i in range(N >> 1):
        G[tmp[i<<1]].append(tmp[(i<<1)+1])
    visit = [False for _ in range(N+1)]
    D = [0 for _ in range(N+1)]

    Q = deque()
    Q.append(start)
    visit[start] = True
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = True
                D[w] = D[v] + 1
    max_distance = max(D)
    max_d_num = 0
    for i in range(N, -1, -1):
        if D[i] == max_distance:
            max_d_num = i
            break
    print('#{} {}'.format(tc, max_d_num))