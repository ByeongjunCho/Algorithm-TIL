# 기울이는 함수
def go(row, col, color, status):
    # status == 1 : 위
    if status == 1:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= i-1 < N and (i-1, j) == hole:
                return (i-1, j)
            elif 0 <= i-1 < N and arr[i - 1][j] == '.':
                i -= 1
            else:
                break
        arr[i][j] = color
    # status == 2: 오
    elif status == 2:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= j+1 < M and (i, j+1) == hole:
                return (i, j+1)
            elif 0 <= j+1 < M and arr[i][j+1] == '.':
                j += 1
            else:
                break
        arr[i][j] = color
    # status == 3: 아
    elif status == 3:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= i+1 < N and (i+1, j) == hole:
                return (i+1, j)
            elif 0 <= i+1 < N and arr[i + 1][j] == '.':
                i += 1
            else:
                break
        arr[i][j] = color
    # status == 4: 왼
    else:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= j-1 < M and (i, j-1) == hole:
                return (i, j-1)
            elif 0 <= j-1 < M and arr[i][j-1] == '.':
                j -= 1
            else:
                break
        arr[i][j] = color
    return (i, j)

def ball(red, blue, status): # 1234=>위오아왼
    if status == 1: # 위
        if red[0] > blue[0]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b
    elif status == 2: # 오
        if red[1] < blue[1]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b
    elif status == 3: # 아
        if red[0] < blue[0]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b
    else:  # 왼
        if red[1] > blue[1]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b

N, M = map(int, (input().split()))
arr = [list(input()) for _ in range(N)]
result = 100
# 파라미터 좌표

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red = (i, j)
        elif arr[i][j] == 'B':
            blue = (i, j)
        elif arr[i][j] == 'O':
            hole = (i, j)



def play(arr, k, br, bb, ar, ab):
    global result
    if ar == hole and ab != hole:
        result = min(result, k)
        return
    elif ab == hole:
        return
    elif k > 10:
        return
    elif br == ar and bb == ab:
        return
    elif k > result:
        return

    for status in range(1, 5):
        r, b = ball(ar, ab, status)
        play(arr, k+1, ar, ab, r, b)
        # 공을 제자리로 돌린다.
        arr[r[0]][r[1]] = '.'
        arr[ar[0]][ar[1]] = 'R'
        arr[b[0]][b[1]] = '.'
        arr[ab[0]][ab[1]] = 'B'


play(arr, 0, (-1, -1), (-1, -1), red, blue)
print(result if result < 11 else -1)