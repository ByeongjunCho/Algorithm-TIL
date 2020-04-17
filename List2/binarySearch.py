def binarySearch(arr, key):
    lo, hi = 0, len(arr) - 1
    # lo: 범위의 시작인덱스, hi: 범위의 끝 인덱스
    while lo <= hi: # 탐색 실패시 lo > hi 성공시 lo==hi
        mid = (lo + hi) >> 1 # //
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1

    return False

def binarySearch(arr, lo, hi, key):

    if lo > hi:
        return False
    mid = (lo + hi) >> 1 # //
    if arr[mid] == key:
        return True
    elif arr[mid] > key:
        return binarySearch(arr, lo, mid - 1, key)
    else:
        return binarySearch(arr, mid+1, hi, key)

