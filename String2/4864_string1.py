# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교


def KMP(pattern, target):
    m = len(pattern)
    pi = [0] * (m+1)
    pi[0] = -1
    i, j = 0, -1
    while i < m:
        while j >= 0 and pattern[i] != pattern[j]:
            j = pi[j]
        i += 1
        j += 1
        pi[i] = j


    i, j = 0, 0
    n = len(target)
    while i < n:
        while j >= 0 and pattern[j] != target[i]:
            j = pi[j]

        i += 1
        j += 1

        if j == m:
            return 1
    return 0


T = int(input())

for test_case in range(1, T + 1):
    pattern = input()
    target = input()

    print('#{} {}'.format(test_case, KMP(pattern, target)))