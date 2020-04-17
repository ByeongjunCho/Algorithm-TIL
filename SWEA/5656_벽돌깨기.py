# 5656. [모의 SW 역량테스트] 벽돌 깨기
from copy import deepcopy

def move(arr):
    for j in range(W):
        for i in range(H-1, -1, -1):
            if arr[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if arr[k][j]:
                        arr[i][j] = arr[k][j]
                        arr[k][j] = 0
                        break

def block(arr, r, c):  # block를 연속으로 파괴
    num = arr[r][c]
    arr[r][c] = 0
    gorow = [r - num + 1, r + num - 1]
    gocol = [c - num + 1, c + num - 1]
    if num > 1:
        for row in range(gorow[0], gorow[1]+1):
            if 0 <= row < H and arr[row][c]:
                block(arr, row, c)
        for col in range(gocol[0], gocol[1]+1):
            if 0 <= col < W and arr[r][col]:
                block(arr, r, col)

def ball(arr, col):
    for i in range(H):
        if arr[i][col]:
            block(arr, i, col)
            move(arr)
            return

def mysum(arr):
    result = 0
    for j in range(W):
        for i in range(H-1, -1, -1):
            if arr[i][j] == 0:
                break
            else:
                result += 1
    return result

def start(k):
    if k == N:
        global result
        arrcopy = deepcopy(arr)
        for idx in s:
            ball(arrcopy, idx)
        result = min(result, mysum(arrcopy))
        return

    for i in range(W):
        s.append(i)
        start(k+1)
        s.pop()


for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    result = 0xffffff
    s = []
    start(0)
    print('#{} {}'.format(tc, result))

