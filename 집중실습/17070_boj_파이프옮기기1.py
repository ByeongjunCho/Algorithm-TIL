def move(y2, x2, mode):  # (y1, x1):파이프 뒤/ (y2, x2): 파이프앞
    if y2 == N-1 and x2 == N-1:
        global result
        result += 1
        return
    if mode == 1 and x2 == N-1:
        return
    if mode == 2 and y2 == N-1:
        return
    # mode
    # 1: 가로, 2: 세로, 3: 대각선
    if mode == 1:
        # 가로로 가는 경우
        if x2+1 < N and not arr[y2][x2+1]:
            move(y2, x2+1, 1)
        # 대각선으로 가는 경우
        if x2+1 < N and y2+1 < N and not arr[y2+1][x2] and not arr[y2+1][x2+1] and not arr[y2][x2+1]:
            move(y2+1, x2+1, 3)
    elif mode == 2:
        # 세로로 가능 경우
        if y2+1 < N and arr[y2+1][x2] == 0:
            move(y2+1, x2, 2)
        # 대각선으로 가능 경우
        if x2 + 1 < N and y2 + 1 < N and not arr[y2 + 1][x2] and not arr[y2 + 1][x2 + 1] and not arr[y2][x2 + 1]:
            move(y2+1, x2+1, 3)
    elif mode == 3:
        # 가로로 가는 경우
        if x2 + 1 < N and not arr[y2][x2 + 1]:
            move(y2, x2 + 1, 1)
        # 세로로 가는 경우
        if y2+1 < N and arr[y2+1][x2] == 0:
            move(y2+1, x2, 2)
        # 대각선으로 가는 경우
        if x2+1 < N and y2+1 < N and not arr[y2+1][x2] and not arr[y2+1][x2+1] and not arr[y2][x2+1]:
            move(y2+1, x2+1, 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
move(0, 1, 1)
print(result)