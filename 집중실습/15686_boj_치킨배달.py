

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue
        elif arr[i][j] == 1:
            house.append((i, j))
        else:
            chicken.append((i, j))

result = 0xffff
order = [0] * M

def combi(k, start, M):
    global result
    if k == M:
        tmp = 0
        for h in house:
            ch_len = 0xffff
            for c in order:
                ch_len = min(ch_len, abs(h[0] - c[0]) + abs(h[1] - c[1]))
            tmp += ch_len

        result = min(tmp, result)
        return

    for i in range(start, len(chicken)):
        order[k] = chicken[i]
        combi(k + 1, i + 1, M)
        order[k] = 0

combi(0, 0, M)
print(result)