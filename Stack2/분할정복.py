# 해결할 문제를 여러 부분으로 나누고 각각 해결하여 통합

arr = [6, 4, 2, 5, 1, 9, 2, 11, 8, 7]

# 재귀호출 구현
def getMin(lo, hi):  # lo: 범위의 시작, hi: 범위의 끝
    if lo == hi:
        return arr[lo]
    mid = (lo + hi) >> 1
    return min(getMin(lo, mid), getMin(mid+1, hi))

def getMin(lo, hi):  # lo: 범위의 시작, hi: 범위의 끝
    if lo == hi:
        return arr[lo]
    return min(getMin(lo, hi-1), getMin(hi, hi))

print(getMin(0, len(arr) - 1))

# 퀵정렬
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)