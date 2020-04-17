# 1259. [S/W 문제해결 응용] 7일차 - 금속막대

from itertools import permutations
import sys
sys.stdin = open('1259_input.txt', 'r')


def PyeonAn(arr, N):
    result_idx = []
    # tmp_arr = []
    # for i in range(N):
    #     tmp_arr.append([arr[2*i], arr[2*i+1]])
    # 첫번째 나사
    odd = [arr[x] for x in range(len(arr)) if not x&1]  # 전
    even = [arr[x] for x in range(len(arr)) if x&1] # 후

    # 머리
    for i in range(0, len(odd)):
        if even.count(odd[i]) == 0:
            result_idx.append(i)
            break

    # 나사를 찾음
    for i in range(len(odd)-1):
        result_idx.append(odd.index(even[result_idx[-1]]))
    result = ''
    for i in range(len(result_idx)):
        result += str(odd[result_idx[i]]) + ' ' + str(even[result_idx[i]]) + ' '

    return result[:-1]


test_case = int(input())
for T in range(1, test_case+1):
    N = int(input())
    test_arr = list(map(int, input().split()))

    print('#{} {}'.format(T, PyeonAn(test_arr, N)))