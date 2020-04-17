# 병합정렬 --> 연결리스트에 적합
# python List append(), pop(), slicing을 사용하면 시간 소요가 높음
# C-style, 배열을 사용하듯이
# arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = [2,2,1,1,3]
tmp = [0] * len(arr)

def mergeSort(lo, hi):    # 문제의 크기 - 정렬할 자료의 범위
    # 기저 사례
    if lo == hi: return

    mid = (lo+hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid+1, hi)
    # 왼쪽과 오른쪽 자료들이 정렬된 상태

    i, j, k = lo, mid+1, lo # i: 왼쪽의 가장 작은 값, j: 오른쪽에서 가장 작은 값, k: tmp 인덱스
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; k, i = k+1, i+1
        else:
            tmp[k] = arr[j]; k, j = k+1, j+1
    # 왼쪽 부분의 값이 남아있는 경우
    while i <= mid:
        tmp[k] = arr[i];
        k, i = k + 1, i + 1
    while j <= hi:
        tmp[k] = arr[j];
        k, j = k + 1, j + 1
    # 정렬된 부분을 옮겨 적음
    for x in range(lo, hi+1):
        arr[x] = tmp[x]

    # 유도 사례


mergeSort(0, len(arr)-1)
print(arr)