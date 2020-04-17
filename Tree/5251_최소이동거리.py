from queue import PriorityQueue
for tc in range(1, 1+int(input())):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))

    visit = [0] * (N+1)
    D = [0xffffff] * (N+1)
    D[0] = 0
    Q = PriorityQueue()
    Q.put((0, 0))

    while not Q.empty():
        d, u = Q.get()
        if d > D[u]: continue
        visit[u] = True

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                Q.put((D[v], v))

    print('#{} {}'.format(tc, D[N]))