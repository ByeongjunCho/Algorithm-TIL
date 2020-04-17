a = [1,2,3,4,5,6,3]

board = [
    [0,0,0,0,0],
[0,1,2,0,0],
[0,0,3,6,0],
[0,0,4,5,0],
[0,0,3,2,1]]

used = [[0 for _ in range(len(board))] for _ in range(len(board))]
dy, dx = [0,0,1,-1], [1,-1, 0, 0]
def f(n, k, i, j):
    if n == k:
        print("존재함")
        return 1
    else:
        used[i][j] = 1
        for idx in range(4):
            wy, wx = dy[idx] + i, dx[idx] + j
            if 0 <= wy < len(board) and 0 <= wx < len(board) and not used[wy][wx] and board[wy][wx] == a[n+1]:
                f(n+1, k, wy, wx)
        used[i][j] = 0

for i in range(5):
    for j in range(5):
        if board[i][j] == a[0]:
            f(0, len(a)-1, i, j)