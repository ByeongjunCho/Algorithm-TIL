# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
import sys
sys.stdin = open('1210_input.txt', 'r')



# 두 개의 조건
# 왼쪽길 등장 : 왼쪽으로 
# 오른쪽 등장 : 오른쪽으로
# 양쪽에 길이 없으면 : 위로


# for _ in range(1, 11):
#     T = input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#     row = 99
#     idx = arr[row].index(2)
#     while row != 0:
#         if idx == 0 and not arr[row][idx+1]:
#             row -= 1
#
#         elif idx == 99 and not arr[row][idx-1]:
#             row -= 1
#
#         elif (idx > 0 and not arr[row][idx-1]) and (idx < 99 and not arr[row][idx+1]):
#             row -= 1
#
#
#         else:
#             if idx > 0 and arr[row][idx-1]:
#                 while arr[row][idx] and idx > -1 :
#                     idx -= 1
#                 row -= 1
#                 idx += 1
#             elif idx < 99 and arr[row][idx+1]:
#                 while idx < 100 and arr[row][idx] :
#                     idx += 1
#                 row -= 1
#                 idx -= 1
#     print('#{} {}'.format(T, idx))

# rowcol = [[0 for _ in range(100)] for _ in range(100)]
def ladder1(arr, row, idx):
    if row == 0:
        return idx
    if idx == 0 and not arr[row][idx+1]:
        return ladder1(arr, row-1, idx)

    elif idx == 99 and not arr[row][idx - 1]:
        return ladder1(arr, row-1, idx)

    elif (idx > 0 and not arr[row][idx - 1]) and (idx < 99 and not arr[row][idx + 1]):
        return ladder1(arr, row-1, idx)
    else:
        if idx > 0 and arr[row][idx-1]:
            while arr[row][idx] and idx > -1:
                idx -= 1
            row -= 1
            idx += 1
        elif idx < 99 and arr[row][idx+1]:
            while idx < 100 and arr[row][idx]:
                idx += 1
            row -= 1
            idx -= 1

        return ladder1(arr, row, idx)

# for _ in range(1, 11):
#     T = input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#     row = 99
#     idx = arr[row].index(2)
#
#     print('#{} {}'.format(T, idx))

# for _ in range(1, 11):
#     T = input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#     row = 99
#     idx = arr[row].index(2)

#     print('#{} {}'.format(T, ladder1(arr, row, idx)))


def DFS(x, y):
    if x == 0:
        return y
    arr[x][y] = 0
    if y-1 >=0 and arr[x][y-1]:
        return DFS(x, y-1)
    elif y+1 <100 and arr[x][y+1]:
        return DFS(x, y+1)
    else:
        return DFS(x-1, y)

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0 # x: 행, y: 열

    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    dir = 0 # 0: 위, 1: 왼쪽, 2: 오른쪽
    while x:
        if dir != 2 and y-1 >= 0 and arr[x][y-1]:
            y, dir = y-1, 1
        elif dir != 1 and y + 1 < 100 and arr[x][y+1]:
            y, dir = y + 1, 2
        else:
            x, dir = x-1, 0
    print(y)