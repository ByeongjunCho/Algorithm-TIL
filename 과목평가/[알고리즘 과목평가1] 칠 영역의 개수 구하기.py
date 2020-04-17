T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        for row in range(x1-1, x2):
            for col in range(y1-1, y2):
                arr[row][col] = 1
    result = 0
    for tmp in arr:
        result += sum(tmp)
    print('#{} {}'.format(tc, result))
