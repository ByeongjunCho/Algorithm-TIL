from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, flag = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):
        for i in range(N):
            if flag == 'up':
                dy = 1
                dx = 0
                start = (0, i)
            elif flag == 'down':
                dy = -1
                dx = 0
                start = (N - 1, i)
            elif flag == 'left':
                dy = 0
                dx = 1
                start = (i, 0)
            elif flag == 'right':
                dy = 0
                dx = -1
                start = (i, N-1)

            Q = deque()
            Q.append(start)
            while Q:
                # if i == 3 and j == 1:
                #     print('//')
                #     pass
                v = Q.popleft()
                w = [v[0] + dy, v[1] + dx]
                if 0 <= w[0] < N and 0 <= w[1] < N:
                    if not arr[v[0]][v[1]] and arr[w[0]][w[1]]: # 0
                        arr[v[0]][v[1]] = arr[w[0]][w[1]]
                        arr[w[0]][w[1]] = 0

                    elif arr[v[0]][v[1]] != 0 and arr[w[0]][w[1]] != 0 and arr[v[0]][v[1]] == arr[w[0]][w[1]] and not visit[v[0]][v[1]]:
                        arr[v[0]][v[1]] += arr[w[0]][w[1]]
                        arr[w[0]][w[1]] = 0
                        visit[v[0]][v[1]] = 1

                    elif arr[v[0]][v[1]] != arr[w[0]][w[1]] and arr[v[0]][v[1]] and arr[w[0]][w[1]]:
                        visit[v[0]][v[1]] = 1

                    Q.append(w)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if j == N-1:
                print(arr[i][j], end='')
            else:
                print(arr[i][j], end=' ')
        print()

