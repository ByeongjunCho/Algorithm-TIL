def quickSort(lo, hi):

    if lo >= hi:
        return
    # 파티션 부분
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    quickSort(lo, i-1)
    quickSort(i+1, hi)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(0, N-1)
    print('#{} {}'.format(tc, arr[N >> 1]))
