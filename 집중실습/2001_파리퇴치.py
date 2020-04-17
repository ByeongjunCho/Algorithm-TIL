T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    slide = N - M + 1
    mymax = 0
    for row in range(slide):
        for col in range(slide):
            fly = 0
            for i in range(M):
                for j in range(M):
                    fly += arr[row+i][col+j]
            mymax = max(mymax, fly)
    print('#{} {}'.format(tc, mymax))
