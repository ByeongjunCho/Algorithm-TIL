# 1208. [S/W 문제해결 기본] 1일차 - Flatten

import sys
sys.stdin = open('input.txt', 'r')
def minmax_index(numbers):
    '''numbers 리스트에 최대/최소
    인덱스를 리턴하는 함수'''
    max_idx = 0
    min_idx = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max_idx]:
            max_idx = i
        if numbers[i] < numbers[min_idx]:
            min_idx = i
    return max_idx, min_idx

for T in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    result = 0
    for _ in range(dump):
        max_ix, min_ix = minmax_index(box_list)
        tmp = box_list[max_ix] - box_list[min_ix]
        if tmp == 0 or tmp == 1:
            break
        box_list[max_ix] -= 1
        box_list[min_ix] += 1
    max_ix, min_ix = minmax_index(box_list)
    print('#{} {}'.format(T, box_list[max_ix] - box_list[min_ix]))
    # print('#{} {}'.format(T, tmp))

# 빈도수 계산
# ex) 0 0 3 1 1 2 1 0 2 1 0
#
# 최대/최소 찾기
# ex)
# 평탄화 작업