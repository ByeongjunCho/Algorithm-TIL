
def postorder(v):
    global N
    if v > N:
        return 0
    if H[v]:
        return H[v]

    left = postorder(v << 1)
    right = postorder((v << 1) + 1)
    H[v] = left + right
    return H[v]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    H = [0] * (N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        H[node] = value
    postorder(1)
    print('#{} {}'.format(tc, H[L]))
