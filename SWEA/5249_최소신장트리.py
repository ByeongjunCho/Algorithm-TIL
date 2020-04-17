# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())

    Edge = [tuple(map(int, input().split())) for _ in range(E)]

    p = [x for x in range(V+1)]

    def findset(x):
        if x != p[x]:
            p[x] = findset(p[x])
        return p[x]

    Edge.sort(key=lambda x: x[2])
    MST = []
    idx = 0
    ww = 0
    while V: # V개의 간선 선택
        u, v, w = Edge[idx]
        # 싸이클 판단
        a = findset(u)
        b = findset(v)
        if a != b:
            p[v] = u
            ww += w
            V -= 1
        idx += 1
    print('#{} {}'.format(tc, ww))