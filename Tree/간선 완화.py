from collections import deque
# 가중치가 없는 경우 BFS를 이용한 거리 계산
def BFS(s):
    D = [0] * (V+1)
    visit = [False] * (V+1)
    Q = deque()
    Q.append(s); visit[s] = True; D[s] = 0

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visit[v]:
                Q.append(v)
                visit[v] = True
                D[v] += D[u] + 1

# 가중치가 존재하는 경우 => BFS를 이용한 brute force 방법
def BFS(s):
    D = [0xffffff] * (V + 1) # D[] 초기값 설정
    # visit = [False] * (V + 1)
    Q = deque()
    Q.append(s)
    D[s] = 0

    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w: # u -> v
                D[v] += D[u] + w
                Q.append(v)

# 가중치가 존재하는 경우 => djikstra를 이용한 방법


def BFS(s):
    D = [0xffffff] * (V + 1) # D[] 초기값 설정
    visit = [False] * (V + 1) # 이미 최단 경로를 찾은 정점들과 아닌 정점들 구분
    D[s] = 0
    cnt = V
    while cnt:
        #아직 최단경로를 찾지 못한 정점 중에서 D[]가 최소인 정점을 찾는다.
        MIN = 0xffffff
        for i in range(V+1):
            if not visit[i] and MIN < D[i]:
                MIN = D[i]
                idx = i

        for v, w in G[idx]:
            if D[idx] + w < D[v]:
                D[v] += D[idx] + w
                visit[v] = True

        cnt -= 1




V, E = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

BFS(0)