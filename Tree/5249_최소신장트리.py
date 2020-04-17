for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

    key = [0xffffff] * (V+1)
    pi = [0] * (V+1)
    visit = [False] * (V+1)
    cnt = V

    key[0] = 0

    while cnt:
        u, MIN = 0, 0xffffff
        for i in range(V+1):
            if not visit[i] and key[i] < MIN:
                u = i
                MIN = key[i]
        visit[u] = True

        for v, w in G[u]:
            if not visit[v] and w < key[v]:
                key[v] = w
                pi[v] = u
        cnt -= 1
    print('#{} {}'.format(tc, sum(key)))