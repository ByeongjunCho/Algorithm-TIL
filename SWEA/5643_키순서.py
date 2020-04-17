# 키 순서
from collections import deque

def graphCount(G, start):
    visit = [0] * len(G)
    Q = deque([start])
    visit[start] = 1
    count = 0
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
                count += 1
    return count

for tc in range(int(input())):
    N = int(input()) # 첫번째 TC의 N
    M = int(input()) # 첫번째 TC의 M
    G = [[] for _ in range(N+1)] # 정방향 그래프
    rG = [[] for _ in range(N+1)] # 역방향 그래프
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        rG[b].append(a)
    count = 0
    for n in range(1, N+1):
        if graphCount(G, n) + graphCount(rG, n) == N-1:
            count += 1
    print('#{} {}'.format(tc+1, count))