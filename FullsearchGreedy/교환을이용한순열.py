arr = [1, 2, 3, 4]
N = len(arr)

def perm(k, n):
    if k == n:
        print(arr)
        return

    for i in range(k, N):
        arr[k], arr[i] = arr[i], arr[k]
        perm(k+1, n)
        arr[k], arr[i] = arr[i], arr[k]


perm(0, N)

def binomical(n, r):
    if n == r or r == 0: return 1
    return binomical(n-1, r-1) + binomical(n-1, r)

print(binomical(5, 3))
print(binomical(10, 3))
print(binomical(35, 10))


# for i in range(N):
#     arr[0], arr[i] = arr[i], arr[0]
#     for k in range(1, N):
#         arr[1], arr[k] = arr[k], arr[1]
#         for j in range(2, N):
#             arr[2], arr[j] = arr[j], arr[2]
#             print(arr)
#             arr[2], arr[j] = arr[j], arr[2]
#         arr[1], arr[k] = arr[k], arr[1]
#     arr[0], arr[i] = arr[i], arr[0]

# def swap(i, j):

# nCr = n-1Cr-1 + c-1Cr
# 5개중 3개 = 특정한 것이 입력된 경우 + 특정한 것이 들어가지 않은 경우
# 5C3 = 4C2 + 4C3
