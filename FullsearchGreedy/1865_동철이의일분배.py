T = int(input())
for tc in range(1, T+1):
    N = int(input())
    workforce = [list(map(int, input().split())) for _ in range(N)]
    maxwork = 0   # 임시값
    order = [0] * N

    # """ greedy로 max값의 근사값을 구한다"""
    # tmp_arr = [[0 for _ in range(N)] for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         tmp_arr[i][j] = workforce[i][j]
    #
    # # 임시변수에서 max값을 찾음
    # for i in range(N):
    #     idx, tmp_max = 0, 0
    #     for j in range(N):
    #         if tmp_arr[i][j] > tmp_max:
    #             idx = j
    #             tmp_max = tmp_arr[i][j]
    #     # 임시 max값을 찾으면 임시 work값에 저장
    #     maxwork *= tmp_max * 0.01
    #     # 해당 idx 아래의 모든 값을 0으로 초기화
    #     for k in range(i, N):
    #         tmp_arr[k][idx] = 0
    #     """ 탐욕으로 max의 근사값 저장 """
    def perm(k, n, used, work):
        global maxwork
        if work < maxwork:
            return
        if k == n:
            maxwork = work
        for i in range(n):
            if used & (1 << i):
                continue
            if workforce[k][i] == 0:
                continue
            perm(k+1, n, used | (1 << i), (workforce[k][i]) * 0.01 * work)
    perm(0, N, 0, 1)
    print('#{} {:.6f}'.format(tc, maxwork*100))