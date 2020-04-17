result = 0
def mergeSort(lo, hi):
    if lo == hi:
        return
    # 분할
    mid = (lo+hi-1) >> 1
    mergeSort(lo, mid)
    mergeSort(mid+1, hi)
    # 왼쪽과 오른쪽이 정렬된 상태
    # 합병과정
    if arr[mid] > arr[hi]:
        global result
        result += 1
    i, j, k = lo, mid+1, lo # 왼쪽 시작값, 오른쪽 시작값, tmp값
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]
        k += 1; i += 1
    while j <= hi:
        tmp[k] = arr[j]
        j += 1
        k += 1
    # tmp 행렬을 원본에 복사한다.
    for x in range(lo, hi+1):
        arr[x] = tmp[x]

def mergeSort(lo, hi):
    global ans
    if lo + 1 == hi: return arr[lo]

    mid = (lo+hi) >> 1

    l = mergeSort(lo, mid)
    r = mergeSort(mid+1, hi)

    if l > r:
        ans += 1
        return l
    else:
        return r

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    mergeSort(0, N-1)
    print('#{} {} {}'.format(tc, arr[N >> 1], result))
    result = 0

