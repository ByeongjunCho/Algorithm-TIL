# def check(N, M):
#     code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
#     code = {code[x]: x for x in range(len(code))}
#     passwords = [0] * 8
#     # 암호가 존재하는 위치 저장
#     ys, ye = 0, 0  # 암호 시작, 암호 끝 행 위치
#     for i in range(N):
#         if ye:
#             break
#         elif not ys and int(arr[i]):
#             ys = i
#         elif ys and not int(arr[i]):
#             ye = i - 1
#
#     xs, xe = 0, 0  # 암호의 끝 열
#     for j in range(M-1, -1, -1):
#         if arr[ys][j] == '1':
#             xe = j
#             break
#
#     xs = xe - 55
#     start = xs
#     for i in range(8):
#         tmp = arr[ys][start:start+7]
#         k = code.get(tmp)
#         if k == None:
#             return 0
#         passwords[i] = k
#         start += 7
#     test = 0
#     for i in range(0, 7, 2):
#         test += passwords[i]
#     test *= 3
#     for i in range(1, 7, 2):
#         test += passwords[i]
#     test += passwords[-1]
#
#     if test % 10:
#         return 0
#
#     for j in range(xs, xe + 1):
#         for i in range(ys, ye):
#             if arr[i][j] != arr[i+1][j]:
#                 return 0
#
#     return sum(passwords)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())  # 세로, 가로
#     arr = [input() for _ in range(N)]
#     print('#{} {}'.format(tc, check(N, M)))



# 간단한 코드
# code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
# code = {code[x]: x for x in range(len(code))}
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())  # 세로, 가로
#     arr = [input() for _ in range(N)]
#
#     def find():
#         # 끝나는 위치를 찾음
#         for i in range(N):
#             for j in range(M-1, 0, -1):
#                 if arr[i][j] == '0': continue
#                 pwd = []
#                 for s in range(j-56+1, j, 7):
#                     pwd.append(code[arr[i][s: s+7]])
#
#                     a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
#                     b = pwd[1] + pwd[3] + pwd[5]
#                     if (a*3 + b) % 10 == 0:
#                         return a+b
#                     else:
#                         return 0
#
#
#     print('#{} {}'.format(tc, find()))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 세로, 가로
    arr = [input() for _ in range(N)]

    def find():
        # 끝나는 위치를 찾음
        for i in range(N):
            j = M - 1
            while j >= 0:
                if arr[i][j] == '1' and arr[i-1][j] == '0':
                    pwd = []
                    for _ in range(8):
                        c2 = c3 = c4 = 0
                        while arr[i][j] == '0': j-1
                        while arr[i][j] == '1': c4, j = c4+1, j-1
                        while arr[i][j] == '0': c3, j = c3 + 1, j - 1
                        while arr[i][j] == '1': c2, j = c2 + 1, j - 1
                        MIN = min(c2, c3, c4)
                        pwd.append(P[(c2//MIN, c3//MIN, c4//MIN)])
                        j -= c1

                    b = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    a = pwd[1] + pwd[3] + pwd[5]
                    if (a*3 + b) % 10 == 0:
                        return a+b
                    else:
                        return 0
