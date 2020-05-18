# 백준 12100번-2084(Easy)

from collections import deque
from copy import deepcopy
# matrix를 해당 방향으로 이동하는 함수
def play(mat, go):
    size = len(mat)
    # go[0,1,2,3] = [왼위오아]

    # 0 왼쪽
    if go == 0:
        for i in range(size):
            Q = deque()
            for j in range(size):
                if mat[i][j]:
                    Q.append(mat[i][j])
                mat[i][j] = 0
            idx = 0
            while Q:
                val = Q.popleft()
                if not mat[i][idx]:
                    mat[i][idx] = val
                elif mat[i][idx] == val:
                    mat[i][idx] *= 2
                    idx += 1
                else:
                    mat[i][idx+1] = val
                    idx += 1

    # 위로
    elif go == 1:
        for j in range(size):
            Q = deque()
            for i in range(size):
                if mat[i][j]:
                    Q.append(mat[i][j])
                mat[i][j] = 0
            idx = 0
            while Q:
                val = Q.popleft()
                if not mat[idx][j]:
                    mat[idx][j] = val
                elif mat[idx][j] == val:
                    mat[idx][j] *= 2
                    idx += 1
                else:
                    mat[idx+1][j] = val
                    idx += 1
    # 오른쪽
    if go == 2:
        # 행순환
        for i in range(size):
            Q = deque()
            # 열순환
            for j in range(size):
                if mat[i][j]:
                    Q.append(mat[i][j])
                mat[i][j] = 0
            idx = size-1
            while Q:
                val = Q.pop()
                if not mat[i][idx]:
                    mat[i][idx] = val
                elif mat[i][idx] == val:
                    mat[i][idx] *= 2
                    idx -= 1
                else:
                    mat[i][idx-1] = val
                    idx -= 1

    # 아래
    elif go == 3:
        # 열순환
        for j in range(size):
            Q = deque()
            for i in range(size):
                if mat[i][j]:
                    Q.append(mat[i][j])
                mat[i][j] = 0
            idx = size-1
            while Q:
                val = Q.pop()
                if not mat[idx][j]:
                    mat[idx][j] = val
                elif mat[idx][j] == val:
                    mat[idx][j] *= 2
                    idx -= 1
                else:
                    mat[idx-1][j] = val
                    idx -= 1



# 중복순열을 만들어서 계산
s = list(range(4))
tmp = []
def back(k):
    if len(tmp) == 5:
        tmp_matrix = deepcopy(matrix)
        for i in tmp:
            play(tmp_matrix, i)
        val = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                val = max(val, tmp_matrix[i][j])

        global result
        result = max(result, val)
        return

    for i in range(4):
        tmp.append(i)
        back(k+1)
        tmp.pop()

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0

back(0)
print(result)


# N = 5
# mat = [[2, 0, 2, 2, 64],
#        [2, 0, 2, 2, 32],
#        [2, 0, 2, 2, 16],
#        [4, 0, 2, 2, 8],
#        [4, 0, 2, 2, 4]]
# play(mat, 3)
# for m in mat:
#     print(m)
# # N = int(input())
# perm(0, mat)
