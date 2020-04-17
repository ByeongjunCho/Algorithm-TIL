def lenth(xy1, xy2):
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

# 순열 만들기
def perm(k, used, before, val):
    global result
    if val > result:
        return
    if k == N:
        result = min(result, val + lenth(before, home))
        return

    for i in range(N):
        if used & (1 << i):
            continue
        if k == 0:
            perm(k+1, used | (1 << i), client[i], val + lenth(work, client[i]))
        else:
            perm(k+1, used | (1 << i), client[i], val + lenth(before, client[i]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    go = list(map(int, input().split()))
    work = (go[0], go[1])
    home = (go[2], go[3])
    client = [0] * N  # 고객 좌표
    idx = 0
    for i in range(4, (N+2)*2, 2):
        client[idx] = (go[i], go[i+1])
        idx += 1
    result = 0xffff
    perm(0, 0, 0, 0)
    print('#{} {}'.format(tc, result))

