from collections import deque
# 최단경로 보장
# Q에 들어간 순서: 방문 순서


def BFS(s):
    # 큐를 생성, 방문표시
    Q = []

    visit = [False] * (V + 1) # 1 ~ V까지
    # 시작점을 방문하고 큐에 삽입
    visit[s] = True; print(s)
    Q.append(s)
    D[s] = 0
    P[s] = s
    # 빈 큐가 아닐 동안
    while Q:
        # 큐에서 하나 꺼내온다. v
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                # v의 방문하지 않은 인접정점을 모두 찾아서
                # 차례로 방문하고 큐에 삽입
                visit[w] = True; print(w)
                D[w] = D[v] + 1  # v->w로 갈 때의 거리 저장
                P[w] = v         # w는 v에서 방문했다는 표시
                Q.append(w)

import sys
sys.stdin = open("BFS_input.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0] * (V + 1)  # 최단거리를 저장하기 위한 배열
P = [0] * (V + 1)  # 최단경로 트리 저장
for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

BFS(1)