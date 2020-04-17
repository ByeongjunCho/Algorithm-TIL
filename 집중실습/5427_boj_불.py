# from collections import deque
import collections
def BFS(sangen, fire, width, height):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    F = collections.deque(fire)
    S = collections.deque(sangen)
    while S:
        # 불 이동
        flen = len(F)
        for _ in range(flen):
            f = F.popleft()
            for i in range(4):
                w = (f[0] + dy[i], f[1] + dx[i])
                if 0 <= w[0] < height and 0 <= w[1] < width and arr[w[0]][w[1]] != '#' and not visit[w[0]][w[1]]: # and arr[w[0]][w[1]] != '@'
                    F.append(w)
                    arr[w[0]][w[1]] = '*'
                    visit[w[0]][w[1]] = 1
        # 상근이 이동
        slen = len(S)
        for _ in range(slen):
            s = S.popleft()
            if s[0] == 0 or s[0] == height - 1 or s[1] == 0 or s[1] == width - 1:
                return D[s[0]][s[1]] + 1
            for i in range(4):
                w = (s[0] + dy[i], s[1] + dx[i])
                if 0 <= w[0] < height and 0 <= w[1] < width and arr[w[0]][w[1]] != '#' and arr[w[0]][w[1]] != '*' and not visit[w[0]][w[1]]:
                    S.append(w)
                    visit[w[0]][w[1]] = 1
                    D[w[0]][w[1]] = D[s[0]][s[1]] + 1
                    if w[0] == 0 or w[0] == height-1 or w[1] == 0 or w[1] == width-1:
                        return D[w[0]][w[1]] + 1

    return 'IMPOSSIBLE'

T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visit = [[0 for _ in range(w)] for _ in range(h)]
    D = [[0 for _ in range(w)] for _ in range(h)]
    fire = [(1001, 1001)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                sangen = (i, j)
            elif arr[i][j] == '*':
                fire.append((i, j))

    print(BFS(sangen, fire, w, h))
