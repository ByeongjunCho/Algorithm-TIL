dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)
s = set()
def backtrack(k, start, num):
    if k == 7:
        s.add(num)
        return
    for i in range(4):
        wy, wx = start[0] + dy[i], start[1] + dx[i]
        if 0 <= wy < 4 and 0 <= wx < 4:
            backtrack(k+1, (wy, wx), num + (10 ** k) * arr[start[0]][start[1]])

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    s = set()
    for i in range(4):
        for j in range(4):
            backtrack(0, (i, j), 0)
    print('#{} {}'.format(tc, len(s)))
