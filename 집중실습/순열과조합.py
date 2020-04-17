def swap(arr, dst, tar):
    a[dst], a[tar] = a[tar], a[dst]
def per(k, N):
    if k == N:
        print(a[0], a[1], a[2])

    for i in range(k, len(a)):
        swap(a, k, i)
        per(k+1, N)
        swap(a, i, k)

per(0, 3)

# 5C3
# arr = 'ABCDE'
# N, R = 5, 3
# choose = []
# def comb(k, start):  # k: 지금까지 선택한 개수, start: 반복문의 시작위치
#     if k == R:
#         print(choose)
#         return
#
#     for i in range(start, N):
#         # i번째 정보를 저장
#         choose.append(arr[i])
#         comb(k+1, i+1)
#         choose.pop()
#
# comb(0, 0)