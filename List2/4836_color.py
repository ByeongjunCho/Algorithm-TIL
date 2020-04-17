# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

import sys
sys.stdin = open('4836_input.txt', 'r')

def color_purple(arr, N):
    test_arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        for j in range(arr[i][0], arr[i][2]+1):
            for k in range(arr[i][1], arr[i][3]+1):
                if (test_arr[j][k] != arr[i][4]):
                    test_arr[j][k] += arr[i][4]

    area = 0
    for i in range(len(test_arr)):
        for j in range(len(test_arr[0])):
            if test_arr[i][j] > 2:
                area += 1
    return area

test_case = int(input())

for T in range(1, test_case+1):
    N = int(input())
    test_arr = []
    for _ in range(N):
        test_arr.append(list(map(int, input().split())))

    print('#{} {}'.format(T, color_purple(test_arr, N)))
