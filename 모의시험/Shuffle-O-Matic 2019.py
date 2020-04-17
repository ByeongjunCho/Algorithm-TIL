# Shuffle-O-Matic 2019


# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr
#
# def shuffle(arr, x):
#     N = len(arr)
#
#     if x == 0:
#         return arr
#     elif x == 1:
#         arr = swap(arr, (len(arr) >> 1) - x, (len(arr) >> 1))
#         return arr
#     elif x == 2:
#         # x == 1 수행
#         arr = swap(arr, (len(arr) >> 1) - x, (len(arr) >> 1) - x + 1)
#         arr = swap(arr, (len(arr) >> 1), (len(arr) >> 1) + x - 1)
#         return arr
#     elif x == 3:
#         # x== 2 수행
#         arr = swap(arr, (len(arr) >> 1) - x, (len(arr) >> 1) - x + 1)
#         arr = swap(arr, (len(arr) >> 1) + x - 2, (len(arr) >> 1) + x - 1)
#         return arr
#     elif x == 4:
#         if x > len(arr):
#             x = x - len(arr)
#         # x == 2 수행
#         return arr
#     elif x == 5:
#         if x > len(arr):
#             x = x - len(arr) - 1
#         # x == 1 수행
#         return arr
def shuffle(arr, x):

    N = len(arr)
    half_N = N >> 1
    mid = (N >> 1) - 1  # 중간부분
    S = []
    left = range(half_N, 0, -1)
    right = range(1, half_N + 1)



def shuffle(arr, x):
    S = []
    N = len(arr)
    half_N = N >> 1
    mid = (N >> 1) - 1  # 중간부분
    left = range(half_N, 0, -1)
    right = range(1, half_N+1)
    if x < half_N:
        status = 0
    else:
        status = 1
        x -= half_N
    i, j = 0, 0
    while i != half_N or j != half_N:
        if not status:
            for _ in range(left[x]):
                if i == half_N:
                    break
                S.append(arr[i])
                i += 1
            S.append(arr[j+half_N])
            j += 1

        elif status:
            for _ in range(right[x]):
                if j == half_N:
                    break
                S.append(arr[j+half_N])
                j += 1
            S.append(arr[i])
            i += 1
    return S

print(shuffle([1,2,3,4,5,6], 5))


