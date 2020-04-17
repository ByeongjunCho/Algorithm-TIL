T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)

    # 이진트리 구현
    i = 1
    while (i << 1) < N+1:
        L[i] = i << 1
        if (i << 1) + 1 < N+1:
            R[i] = (i << 1) + 1
        i += 1
