from collections import deque
maxlen = 100001
def BFS(dst, tar):
    Q = deque()
    Q.append(dst)
    D = [0] * maxlen
    D[dst] = 1

    while Q and not D[tar]:
        v = Q.popleft()
        if v+1 < maxlen and not D[v+1]:
            w = v+1
            D[w] = D[v] + 1
            Q.append(w)
        if v-1 >= 0 and not D[v-1]:
            w = v-1
            D[w] = D[v] + 1
            Q.append(w)
        if 2*v < maxlen and not D[2*v]:
            w = 2*v
            D[w] = D[v] + 1
            Q.append(w)
    return D[tar]


N, K = map(int, input().split())
print(BFS(N, K) - 1)
