arr = [list(map(int, input().split())) for _ in range(9)]
# 딕셔너리 생성. key는 좌표, 값은 들어갈 수 있는 후보군
dictionary = {}
# 가로 확인
for i in range(9):
    xy = []  # 값이 0인 좌표 저장
    val = set() # 들어갈 수 있는 후보군 저장
    tmp = [0] * 10
    for j in range(9):
        if arr[i][j] == 0:
            xy.append((i, j))
        else:
            tmp[arr[i][j]] = 1
    for k in range(1, 10):
        if not tmp[k]:
            val.add(k)
    # 좌표값과 후보군을 입력
    for kk in xy:
        if dictionary.get(kk):
            dictionary[kk] = dictionary.get(kk).intersection(val)
        else:
            dictionary[kk] = val
# # 세로 확인
# for i in range(9):
#     xy = []  # 값이 0인 좌표 저장
#     val = set() # 들어갈 수 있는 후보군 저장
#     tmp = [0] * 10
#     for j in range(9):
#         if arr[j][i] == 0:
#             xy.append((j, i))
#         else:
#             tmp[arr[j][i]] = 1
#     for k in range(1, 10):
#         if not tmp[k]:
#             val.add(k)
#     # 좌표값과 후보군을 입력
#     for kk in xy:
#         if dictionary.get(kk):
#             dictionary[kk] = dictionary.get(kk).intersection(val)
#         else:
#             dictionary[kk] = val
# # 정사각형 확인
# d = [0, 3, 6]
# for i in d:
#     for j in d:
#         xy = []  # 값이 0인 좌표 저장
#         val = set()  # 들어갈 수 있는 후보군 저장
#         tmp = [0] * 10
#         for ii in range(3):
#             for jj in range(3):
#                 if arr[i + ii][j + jj] == 0:
#                     xy.append((i + ii, j + jj))
#                 else:
#                     tmp[arr[i + ii][j + jj]] = 1
#
#         for k in range(1, 10):
#             if not tmp[k]:
#                 val.add(k)
#         # 좌표값과 후보군을 입력
#         for kk in xy:
#             if dictionary.get(kk):
#                 dictionary[kk] = dictionary.get(kk).intersection(val)
#             else:
#                 dictionary[kk] = val
# 저장된 좌표 중에서 후보군이 1개인 경우는 제거
keys = list(dictionary.keys())
for key in keys:
    if len(dictionary[key]) == 1:
        y, x = key
        val = dictionary.pop(key).pop()
        arr[y][x] = val

def check_sudoku(row, col):
    # 가로 확인
    tmp = [0] * 10
    for i in range(9):
        tmp[arr[i][col]] = 1
    for k in range(1,10):
        if tmp[k] == 2:
            return False
    if tmp[0]:
        return True

    # 세로 확인
    tmp = [0] * 10
    for i in range(9):
        tmp[arr[row][i]] = 1
    for k in range(1, 10):
        if tmp[k] == 2:
            return False
    if tmp[0]:
        return True

    return True
dic_keys = list(dictionary.keys())
N = len(dic_keys)

def backtrack(k):
    if k > N-1:
        return
    for val in dictionary[dic_keys[k]]:
        y, x = dic_keys[k]
        arr[y][x] = val
        if check_sudoku(y,x):
            backtrack(k+1)
        else:
            arr[y][x] = 0

def print_array():
    for i in range(9):
        tmp = list(map(str, arr[i]))
        print(' '.join(tmp))

if len(dic_keys) == 0:
    print_array()
else:
    backtrack(0)
    print_array()