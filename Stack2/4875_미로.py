# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

def func(arr, N):
    status = [[-1, 0], [0, 1], [0, 0], [1, 0], [0,-1]]  #
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i,j]
                break
    # start = [N - 1, arr[N - 1].index(2)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    S = [start]
    v = start
    while S:
        for w in status:
            if 0 <= v[0] + w[0] < N and 0 <= v[1] + w[1] < N:
                if not visit[v[0] + w[0]][v[1] + w[1]]:
                    if arr[v[0] + w[0]][v[1] + w[1]] != 1:
                        if arr[v[0] + w[0]][v[1] + w[1]] == 3:
                            return 1
                        visit[v[0]][v[1]] = 1
                        S.append(v)
                        v = [v[0] + w[0], v[1] + w[1]]
                        break
        else:
            v = S.pop()
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기
    # arr = [list(map(int, input().split())) for _ in range(N)]
    arr = [list(map(int, list(input()))) for _ in range(N)]
    print('#{} {}'.format(tc, func(arr, N)))




