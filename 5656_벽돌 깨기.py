# 5656. [모의 SW 역량테스트] 벽돌 깨기
from collections import deque

def boom(y, x, width, height, br, Q):
    if br[y][x] == 0:
        return
    length = br[y][x]
    for i in range(y-length+1, y+length):
        if not 0 <= i < height or i == y:
            continue
        if br[i][x] == 1:
            br[i][x] = 0
        elif br[i][x]:
            Q.append([i, x])
    for j in range(x-length+1, x+length):
        if not 0 <= j < width or j == x:
            continue
        if br[y][j] == 1:
            br[y][j] = 0
        elif br[y][j]:
            Q.append([y, j])
    br[y][x] = 0

def remove(c, br, width, height, Q): # 공을 떨구는 열
    for y in range(H):
        if br[y][c]:
            Q.append([y, c])
            while Q:
                y, x = Q.popleft()
                boom(y, x, width, height, br, Q)
            break
    # 남은 공을 내림
    for w in range(width):
        tmp = []
        for h in range(height):
            if br[h][w]:
                tmp.append(br[h][w])
                br[h][w] = 0
        rh = height-1
        while tmp:
            br[rh][w] = tmp.pop()
            rh -= 1


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    minVal = 0xffffff
    p = [0] * N
    def perm(k, N, width, height):
        if k == N:
            copyarr = [[0 for _ in range(width)] for _ in range(height)]
            # 복사
            Q = deque()
            for i in range(H):
                for j in range(W):
                    copyarr[i][j] = arr[i][j]
            for c in p:
                remove(c, copyarr, width, height, Q)
            cnt = 0
            for i in range(height):
                for j in range(width):
                    if copyarr[i][j]:
                        cnt += 1
            global minVal
            minVal = min(minVal, cnt)
            return

        for i in range(width):
            p[k] = i
            perm(k+1, N, width, height)
    perm(0, N, W, H)
    print("#{} {}".format(tc, minVal))