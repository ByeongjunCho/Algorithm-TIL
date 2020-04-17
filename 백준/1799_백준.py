def chess(row, col):
    dy = [-1, -1, 1, 1]
    dx = [1, -1, -1, 1]
    if arr[row][col] == 0:
        return False
    for k in range(4):
        i, j = row, col
        wy, wx = i + dy[k], j+dx[k]
        while 0 <= wy < N and 0 <= wx < N:
            if arr[wy][wx] == 0 or arr[wy][wx] == 1:
                wy, wx = wy + dy[k], wx + dx[k]
            else:
                return False
            # elif arr[wy][wx] == 'B':
            #     return False

    return True

def backtrack(k, cnt):
    global result
    if len(bishop) - 1 - k < result - cnt:
        return
    if k > len(bishop)-1:
        result = max(cnt, result)
        return

    # 비숍을 넣는 경우
    y, x = bishop[k]
    tmp = arr[y][x]
    if chess(y,x):
        arr[y][x] = 'B'
        backtrack(k+1, cnt+1)

    # 비숍을 넣지 않는 경우
    arr[y][x] = tmp
    backtrack(k+1, cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]



# 후보좌표 입력
bishop = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bishop.append((i, j))
result = 0
backtrack(0, 0)
print(result)