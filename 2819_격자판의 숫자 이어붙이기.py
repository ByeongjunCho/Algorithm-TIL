# 2819. 격자판의 숫자 이어 붙이기

# T = int(input())
#
# for tc in range(1, T+1):
#     # arr = [list(map(int, input().split())) for _ in range(4)]
#     arr = [list(input().split()) for _ in range(4)]
#     dy = [1, -1, 0, 0]
#     dx = [0, 0, 1, -1]
#     result = set()
#     temp = [0] * 7
#     def dfs(k, y, x):
#         if k == 7:
#             result.add(''.join(temp))
#             return
#         for i in range(4):
#             wy, wx = dy[i] + y, dx[i] + x
#             if 0 <= wy < 4 and 0 <= wx < 4:
#                 temp[k] = arr[y][x]
#                 dfs(k+1, wy, wx)
#     for i in range(4):
#         for j in range(4):
#             dfs(0, i, j)
#
#     print("#{} {}".format(tc, len(result)))


"""강의코드"""
T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    result = set()
    def dfs(k, y, x, val):
        if k == 7:
            result.add(val)
            return

        for i in range(4):
            wy, wx = dy[i] + y, dx[i] + x
            if 0 <= wy < 4 and 0 <= wx < 4:
                dfs(k+1, wy, wx, val+(arr[y][x] * 10**k))
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, 0)
    print("#{} {}".format(tc, len(result)))