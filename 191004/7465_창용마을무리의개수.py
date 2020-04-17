from collections import deque
def bfs(start):
    Q = deque()
    Q.append(start)
    visit[start] = 1
    flag = 0
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                flag = 1
                visit[w] = 1
                Q.append(w)
    # if flag:
    #     return 1
    # else:
    #     return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    visit = [0] * (N+1)
    result = 0  # 결과값 저장
    for i in range(1, N+1):
        if not visit[i]:
            result += bfs(i)
    print('#{} {}'.format(tc, result))