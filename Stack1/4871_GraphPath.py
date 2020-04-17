T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    # 간선 정보
    for _ in range(E):
        s, e= map(int, input().split())
        G[s].append(e)
    # 방문 확인
    visit = [False] * (V+1)
    # 확인을 위한 데이터값
    start, target = map(int, input().split())
    result = 0

    S = [start]
    visit[start] = True
    while S:
        for w in G[start]:
            if not visit[w]:
                visit[w] = True
                S.append(w)
                if w == target:
                    result = 1
                    S.clear()
                    break
                start = w
                break
        else:
            start = S.pop()
    print('#{} {}'.format(tc, result))
