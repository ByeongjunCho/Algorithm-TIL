# 1209. [S/W 문제해결 기본] 2일차 - Sum
import sys
sys.stdin = open('input.txt', 'r')

def my_max(arr):
    max_val = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def my_sum(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]

    return result


# def arr_max(arr):
#
#     tmp = 0 # 대각선
#     tmp_sum = 0
#     # 행에 있는 값 더하기
#     for row in range(len(arr)):
#         result = 0
#         for col in range(len(arr[0])):
#             result += arr[row][col]
#             # 아래 하단으로 대각선
#             if row == col:
#                 tmp += arr[row][col]
#         if result > tmp_sum:
#             tmp_sum = result
#     if tmp > tmp_sum:
#         tmp_sum = tmp
#
#     # 열에 있는 값 더하기
#     tmp = 0
#     for col in range(len(arr[0])):
#         result = 0
#         for row in range(len(arr)):
#             result += arr[row][col]
#             if row+col == 99:
#                 tmp += arr[row][col]
#         if result > tmp_sum:
#             tmp_sum = result
#     if tmp > tmp_sum:
#         tmp_sum = tmp
#
#     return tmp_sum


def arr_max(arr):
    Max = 0

    for i in range(100):
        rsum = csum = 0
        dsum1 = dsum2 = 0  # 대각합
        dsum1 += arr[i][i]
        dsum2 += arr[i][99-i]
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        Max = max(Max, rsum, csum)
    Max = max(Max, dsum1, dsum2)
    return Max




# def arr_max(arr):
#     tmp1 = 0  # 대각선
#     tmp2 = 0
#     tmp_max = 0  # 최대값
#     tmp_col = [0]*100 # 열값을 담을 list
#     # 행에 있는 값 더하기
#     for row in range(len(arr)):
#         result = 0
#         for col in range(len(arr[0])):
#             result += arr[row][col]
#             # 열값은 임시 리스트에 따로 저장
#             tmp_col[col] += arr[row][col]
#             # 오른쪽 아래로 대각선
#             if row == col:
#                 tmp1 += arr[row][col]
#             # 왼쪽 상단 대각선
#             if row + col == 99:
#                 tmp2 += arr[row][col]
#         # 최대값 판단
#         if result > tmp_max:
#             tmp_max = result
#     # 대각값 최대 판단
#     if tmp1 > tmp_max:
#         tmp_max = tmp1
#     if tmp2 > tmp_max:
#         tmp_max = tmp2
#
#     # 열우선 순회 값 최대판단
#     col_max = my_max(tmp_col)
#     if tmp_max > col_max:
#         return tmp_max
#     else:
#         return col_max




for _ in range(10):
    T = int(input())  # 테스트 케이스의 번호
    # 행렬 입력
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    print('#{} {}'.format(T, arr_max(arr)))
