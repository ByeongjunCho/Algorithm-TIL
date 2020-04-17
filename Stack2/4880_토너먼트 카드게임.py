# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

def func(arr, i, j):
    if i == j:
        return i

    result_left = func(arr, i, (i + j) // 2)
    result_right = func(arr, (i + j) // 2 + 1, j)

    if arr[result_left] == arr[result_right]:
        return result_left
    else:
        if arr[result_left] == 1 and arr[result_right] == 3:
            return result_left
        elif arr[result_left] == 3 and arr[result_right] == 1:
            return result_right
        else:
            if arr[result_left] > arr[result_right]:
                return result_left
            else:
                return result_right

def divide(lo, hi):
    print(lo, hi)
    if lo == hi:
        return

    mid = (lo + hi) >> 1
    # 왼쪽 lo ~ mid, 오른쪽 mid + 1 ~ hi
    divide(lo, mid)
    divide(mid + 1, hi)


divide(0, 7)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print('#{} {}'.format(tc, func(arr, 0, N-1)+1))

