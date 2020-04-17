# 2805. 농작물 수확하기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    for i in range(N):
        if i > (N >> 1):
            k = i - (N >> 1)
        else:
            k = (N >> 1) - i
        for j in range(k, N - k):
            result += farm[j][i]
    print('#{} {}'.format(tc, result))
