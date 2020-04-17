from collections import deque

def bfs(start, dst, N):
    if start == dst:
        return 0
    Q = deque()
    Q.append(start)
    move = ((-2,1), (-1,2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    while Q:
        v = Q.popleft()
        for k in move:
            wy, wx = v[0] + k[0], v[1] + k[1]
            if 0 <= wy < N and 0 <= wx < N and not D[wy][wx]:
                D[wy][wx] = D[v[0]][v[1]] + 1
                if (wy, wx) == dst:
                    return D[wy][wx]
                Q.append((wy, wx))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sta = tuple(map(int, input().split()))
    dst = tuple(map(int, input().split()))
    D = [[0 for _ in range(N)] for _ in range(N)]
    print(bfs(sta, dst, N))