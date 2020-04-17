''' 본인 풀이 - convolution 연산을 기초로 하여 작성(매우 느림)'''
# def conv(window, filter, K):
#     row = len(window)
#     col = row
#     w_r = len(filter)
#     w_c = w_r
#     slide = row
#     result = 0  # 집의 최대값 출력
#     for r in range(1-K, slide):
#         for c in range(1-K, slide):
#             house = 0
#             for i in range(w_r):
#                 for j in range(w_c):
#                     if 0 <= r+i < row and 0 <= c+j < col:
#                         house += window[r+i][c+j]*filter[i][j]
#             result = max(result, house)
#     return result
#
# def makefilter(K):
#     N = 2*(K-1) + 1
#     vec2 = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N//2):
#         count = 2*i + 1
#         for j in range(K-i-1, N):
#             vec2[i][j] = 1
#             count -= 1
#             if not count:
#                 break
#     c = N
#     for i in range(N//2, N):
#         count = c
#         for j in range(i-K+1, N):
#             vec2[i][j] = 1
#             count -= 1
#             if not count:
#                 break
#         c -= 2
#     return vec2
#
#
#
# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     K = N+2
#     bhouse = 0
#     while K:
#         fil = makefilter(K)
#         house = conv(arr, fil, K)
#         if house * M >= K*K + (K-1)*(K-1):
#             bhouse = house
#             break
#         else:
#             # bhouse = house
#             K -= 1
#     print('#{} {}'.format(tc, bhouse))


''' 집 위치를 이용한 풀이'''
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    house = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                house.append((i, j))

    def result():
        K = N + 1
        while K:
            result = 0
            cost = K*K+(K-1)**2
            for i in range(N):
                for j in range(N):
                    count = 0
                    for h in house:
                        if abs(i - h[0]) + abs(j - h[1]) < K:
                            count += 1
                    result = max(result, count)
            if result * M >= cost:
                return result
            K -= 1


    print('#{} {}'.format(tc, result()))