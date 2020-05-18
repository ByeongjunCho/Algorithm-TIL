# 백준 12100번-2048(Easy)

# 좌우변환
def reverse(mat):
    for i in range(len(mat)):
        mat[i] = mat[i][::-1]


# 전치행렬변환
def transpose(mat):
    # 복사
    tmpmat = [x[:] for x in mat]
    for j in range(len(mat)):
        for i in range(len(mat)):
            mat[i][j] = tmpmat[j][i]

def shift(mat):
    for i in range(len(mat)):
        tmp = []
        for j in range(len(mat)-1, -1, -1):
            if mat[i][j]:
                tmp.append(mat[i][j])
            mat[i][j] = 0 # 0으로 초기화
        idx = 0
        while tmp:
            val = tmp.pop()
            if mat[i][idx] == 0:
                mat[i][idx] = val
            elif mat[i][idx] and mat[i][idx] == val:
                mat[i][idx] *= 2
                idx += 1
            else:
                mat[i][idx+1] = val
                idx += 1

def play(mat, sign):
    # 0123 == 왼위오아
    tmpmat = [x[:] for x in mat]  # 복사
    if sign == 0: # 왼쪽
        shift(tmpmat)
    elif sign == 1: # 위
        transpose(tmpmat)
        shift(tmpmat)
        transpose(tmpmat)
    elif sign == 2: # 오른쪽
        reverse(tmpmat)
        shift(tmpmat)
        reverse(tmpmat)
    elif sign == 3: # 아래
        transpose(tmpmat)
        reverse(tmpmat)
        shift(tmpmat)
        reverse(tmpmat)
        transpose(tmpmat)

    return tmpmat


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0
def solve(k, mat):
    if k == 5:
        global result
        result = max(result, max([max(x) for x in mat]))
        return

    left = play(mat, 0)
    top = play(mat, 1)
    right = play(mat, 2)
    bottom = play(mat, 3)

    solve(k+1, left)
    solve(k+1, top)
    solve(k+1, right)
    solve(k+1, bottom)

solve(0, matrix)
print(result)