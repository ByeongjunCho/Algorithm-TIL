arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
one = []  # 1의 좌표


# 1. 찾는다
# 2. 지운다. 종이 사용
# 3. 다시 복구


def isPaper(row, col, mode):
    if row + mode > 10 or col + mode > 10:
        return False
    for i in range(row, row+mode):
        for j in range(col, col+mode):
            if not arr[i][j]:
                return False

    return True

def setPaper(row, col, mode, val):
    for i in range(row, row+mode):
        for j in range(col, col+mode):
            arr[row][col] = val

def paper():

    for mode in range(5, 0, -1):
        # 색종이를 5부터 1까지 확인
        for i in range(10):
            if not paper[mode]:
                break
            for j in range(10):
                if isPaper(i, j, mode):
                    if not paper[mode]:
                        break
                    paper[mode] -= 1
                    setPaper(i, j, mode, 0)
                    paper()
                    paper[mode] += 1
                    setPaper(i, j, mode, 1)