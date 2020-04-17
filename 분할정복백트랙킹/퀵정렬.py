arr = [69, 10, 30, 2, 16, 8, 31, 22]

def quickSort(lo, hi):  # Hoare-Partition 알고리즘(가장 왼쪽을 pivot로 설정)
    if lo >= hi: return

    # 피봇을 정해서 partition 알고리즘 수행
    i, j = lo, hi   # arr[lo]: 피봇
    while i < j:
        while i <= hi and arr[lo] >= arr[i]: i+=1
        while arr[lo] < arr[j]: j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo] # 피봇의 위치를 조정
    quickSort(lo, j-1)
    quickSort(j+1, hi)

def quickSort(lo, hi):  # romute-Partition 알고리즘(가장 왼쪽을 pivot로 설정)
    if lo >= hi: return


    i = lo - 1
    for j in range(lo, hi):  # lo ~ hi-1  arr[hi]: pivot
        if arr[j] < arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    quickSort(lo, i-1)
    quickSort(i+1, hi)

quickSort(0, len(arr)-1)
print(arr)

