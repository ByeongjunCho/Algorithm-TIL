# 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            if box[i][j]:
                col += 1
            else:
                if col == K:
                    result += 1
                    col = 0
                else:
                    col = 0
            if box[j][i]:
                row += 1
            else:
                if row == K:
                    result += 1
                    row = 0
                else:
                    row = 0
        if row == K:
            result += 1
        if col == K:
            result += 1
    print('#{} {}'.format(tc, result))