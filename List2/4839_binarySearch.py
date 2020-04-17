# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색


def bSearchCount(page, key):
    start, stop = 0, page
    count = 0

    while start <= stop:

        mid = (start + stop) >> 1

        if mid > key:
            stop = mid
        else:
            start = mid

        if mid == key:
            return count
        count += 1

    return count



test_case = int(input())
for T in range(1, test_case+1):
    P, Pa, Pb = map(int, input().split())
    countA = bSearchCount(P, Pa)
    countB = bSearchCount(P, Pb)

    if countA == countB:
        status = '0'
    elif countA < countB:
        status = 'A'
    else:
        status = 'B'

    print('#{} {}'.format(T, status))
