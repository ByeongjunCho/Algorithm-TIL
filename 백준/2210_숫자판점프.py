result = set()
numbers = [0] * 6
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def arr_comb(k, v):
    if k == 6:
        result.add(tuple(numbers))
        return
    for i in range(4):
        wy, wx = v[0] + dy[i], v[1] + dx[i]
        if 0 <= wy < 5 and 0 <= wx < 5:
            numbers[k] = arr[v[0]][v[1]]
            arr_comb(k+1, (wy, wx))

arr = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        arr_comb(0, (i, j))

print(len(result))
