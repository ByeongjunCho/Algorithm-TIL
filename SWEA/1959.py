# 두 개의 숫자열

def conv(arr1, arr2, arr1_size, arr2_size):
    result = -1e10 # 정답 출력 그릇
    if arr1_size >= arr2_size:
        tar_arr, dst_arr = arr1, arr2
        slide = arr1_size - arr2_size + 1
        dst_size = arr2_size
    else:
        tar_arr, dst_arr = arr2, arr1
        slide = arr2_size - arr1_size + 1
        dst_size = arr1_size

    for s in range(slide):
        
        tmp = 0
        for win in range(dst_size):
            tmp += tar_arr[s+win] * dst_arr[win]
        result = tmp if tmp > result else result
    
    return result

case = int(input())
for T in range(1, case+1):
    arr1_size, arr2_size = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(f'#{T} {conv(arr1, arr2, arr1_size, arr2_size)}')