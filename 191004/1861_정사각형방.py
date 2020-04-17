dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

def room(start):
    for i in range(4):
        wy, wx = dy[i] + start[0], dx[i] + start[1]
        if 0 <= wy < N and 0 <= wx < N and arr[start[0]][start[1]] + 1 == arr[wy][wx]:
            visit[wy][wx] = 1
            global result
            result += 1
            room((wy, wx))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [0] * (N**2 + 1)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    # 거리 계산
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                result = 1
                room((i, j))
                distance[arr[i][j]] = result
    # 최대값과 인덱스 출력
    idx = -1
    MAX = 0
    for i in range(N**2, -1, -1):
        if distance[i] >= MAX:
            idx = i
            MAX = distance[i]
    print('#{} {} {}'.format(tc, idx, MAX))