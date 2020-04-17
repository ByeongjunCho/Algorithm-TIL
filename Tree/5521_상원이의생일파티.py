from collections import deque
for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    D = [0] * (N+1)     # 거리 저장
    visit = [0] * (N+1)
    Q = deque()
    Q.append(1)
    flag = 1
    visit[1] = 1
    while flag and Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = 1
                D[w] = D[v] + 1
                Q.append(w)
                if D[w] > 2:
                    flag = 0
    result = 0
    for i in range(N+1):
        if D[i] == 1 or D[i] == 2:
            result += 1

    print('#{} {}'.format(tc, result))






