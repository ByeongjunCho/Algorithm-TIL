# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

def sel_sort(arr):
    tmp = ''
    for i in range(5):
        min_idx = i*2
        max_idx = i*2
        for j in range(i*2, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            if arr[max_idx] < arr[j]:
                max_idx = j
        tmp += str(arr[max_idx]) +' ' + str(arr[min_idx]) + ' '
        arr[2*i+1], arr[min_idx] = arr[min_idx], arr[2*i+1]
        arr[2*i], arr[max_idx] = arr[max_idx], arr[2*i]
    return tmp[0:-1]


    # for i in range(len(arr)-1):
    #     min_idx = i
    #     for j in range(i+1, len(arr)):
    #         if arr[min_idx] > arr[j]:
    #             min_idx = j
    #     arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # return arr


test_case = int(input())
for T in range(1, test_case+1):
    N = int(input())
    test_arr = list(map(int, input().split()))

    print('#{} {}'.format(T, sel_sort(test_arr)))


