# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, numbers[M % N]))