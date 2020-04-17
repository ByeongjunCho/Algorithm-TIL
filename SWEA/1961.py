# 숫자 배열 회전

def rotate_90(arr, arr_size):  # arr은 2차원 배열
    result_arr = []
    for width in range(arr_size):
        
        tmp_arr = []
        for height in range(arr_size-1, -1, -1):
            tmp_arr.append(arr[height][width])
        result_arr.append(tmp_arr)

    return result_arr

case = int(input())

for T in range(1, case+1):
    arr_size = int(input())
    target_arr = []
    for _ in range(arr_size):
        target_arr.append(list(map(int, input().split())))
    
    l_90 = rotate_90(target_arr, arr_size)
    print(l_90)
    l_180 = rotate_90(l_90, arr_size)
    l_270 = rotate_90(l_180, arr_size)

    print(f'#{T}')
    for height in range(arr_size):
        for width in range(arr_size):
            print(f'{l_90[height][width]}', end='')
        print('', end=' ')
        for width in range(arr_size):
            print(f'{l_180[height][width]}', end='')
        print('', end=' ')
        for width in range(arr_size):
            print(f'{l_270[height][width]}', end='')
        print('')