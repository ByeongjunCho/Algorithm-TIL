T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [0] * (N+1)
    # 이진트리 구현

    H = [0] * (N+1)
    nums = list(map(int, input().split()))
    top = 0
    for item in nums:
        top += 1
        H[top] = item
        c, p = top, top // 2
        while p:
            if H[p] > H[c]:
                H[p], H[c] = H[c], H[p]
                c = p
                p = c // 2
            else:
                break

    result = 0
    while N > 0:
        N = N >> 1
        result += H[N]
    print('#{} {}'.format(tc, result))