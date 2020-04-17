import sys
sys.stdin = open('1204.txt', 'r')

code = {
    (2,1,1): 0, (2,2,1): 1, (1,2,2): 2, (4,1,1): 3, (1,3,2): 4,
    (2,3,1): 5, (1,1,4): 6, (3,1,2): 7, (2,1,3): 8, (1,1,2): 9
        }
def get_code(N, M):

    result = 0
    for i in range(1, N):
        j = M-1
        flag = 0
        while j >= 0:
            if arr[i][j] != '0' and arr[i-1][j] == '0':
                tmp_bin = ''
                # 16진수를 4자리 이진수로 변환하여 저장
                while j >= 0 and arr[i-1][j] == '0':
                    a = bin(int(arr[i][j], 16))[2:]
                    if len(a) == 1:
                        a = '000' + a
                    elif len(a) == 2:
                        a = '00' + a
                    elif len(a) == 3:
                        a = '0' + a
                    tmp_bin = a + tmp_bin
                    j -= 1
                tmp_bin = int(tmp_bin, 2)
                

                while tmp_bin & 1 == 0:
                    tmp_bin = tmp_bin >> 1

                while tmp_bin:
                    secret = [0] * 8
                    for k in range(7,-1,-1):
                        c1 = c2 = c3 = 0
                        # print('ori', bin(tmp_bin))
                        while tmp_bin & 1 == 1:
                            c3 += 1
                            tmp_bin = tmp_bin >> 1
                        # print('c3', bin(tmp_bin))
                        while tmp_bin & 1 == 0:
                            c2 += 1
                            tmp_bin = tmp_bin >> 1
                        # print('c2', bin(tmp_bin))
                        while tmp_bin & 1 == 1:
                            c1 += 1
                            tmp_bin = tmp_bin >> 1
                        # print('c1', bin(tmp_bin))
                        while tmp_bin & 1 == 0:
                            if not tmp_bin:
                                break
                            tmp_bin = tmp_bin >> 1

                        MIN = min(c1, c2, c3)
                        # print(c1, c2, c3)
                        # secret[k] = code.get((c1/MIN,c2/MIN,c3/MIN))
                        secret[k] = code[(c1 / MIN, c2 / MIN, c3 / MIN)]

                    test = secret[0] + secret[2] + secret[4] + secret[6]
                    test *= 3
                    test += secret[1] + secret[3] + secret[5]
                    test += secret[7]
                    if test % 10 == 0:
                        result += sum(secret)
            else:
                j -= 1
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 세로, 가로

    arr = [input() for _ in range(N)]
    print('#{} {}'.format(tc, get_code(N, M)))



# import sys
# sys.stdin = open('1204.txt', 'r')

# code = {
#     (2,1,1): 0, (2,2,1): 1, (1,2,2): 2, (4,1,1): 3, (1,3,2): 4,
#     (2,3,1): 5, (1,1,4): 6, (3,1,2): 7, (2,1,3): 8, (1,1,2): 9
#         }
# def get_code(N, M):
#     result = 0
#     for i in range(1, N):
#         j = M-1
#         while j >= 0:
#             if arr[i][j] != '0' and arr[i-1][j] == '0':
#                 tmp_bin = ''
#                 # 16진수를 4자리 이진수로 변환하여 저장
#                 while j >= 0:
#                     a = bin(int(arr[i][j], 16))[2:]
#                     if len(a) == 1:
#                         a = '000' + a
#                     elif len(a) == 2:
#                         a = '00' + a
#                     elif len(a) == 3:
#                         a = '0' + a
#                     tmp_bin = a + tmp_bin
#                     j -= 1
#                 tmp_bin = int(tmp_bin, 2)
#
#                 while tmp_bin & 1 == 0:
#                     tmp_bin = tmp_bin >> 1
#
#                 secret = [0] * 8
#                 for k in range(7,-1,-1):
#                     c1 = c2 = c3 = 0
#                     # print('ori', bin(tmp_bin))
#                     while tmp_bin & 1 == 1:
#                         c3 += 1
#                         tmp_bin = tmp_bin >> 1
#                     # print('c3', bin(tmp_bin))
#                     while tmp_bin & 1 == 0:
#                         c2 += 1
#                         tmp_bin = tmp_bin >> 1
#                     # print('c2', bin(tmp_bin))
#                     while tmp_bin & 1 == 1:
#                         c1 += 1
#                         tmp_bin = tmp_bin >> 1
#                     # print('c1', bin(tmp_bin))
#                     while tmp_bin & 1 == 0:
#                         if not tmp_bin:
#                             break
#                         tmp_bin = tmp_bin >> 1
#
#                     MIN = min(c1, c2, c3)
#                     # print(c1, c2, c3)
#                     secret[k] = code.get((c1//MIN,c2//MIN,c3//MIN))
#
#                 test = secret[0] + secret[2] + secret[4] + secret[6]
#                 test *= 3
#                 test += secret[1] + secret[3] + secret[5]
#                 test += secret[7]
#                 if test % 10 == 0:
#                     result += sum(secret)
#                     print(secret)
#
#             else:
#                 j -= 1
#     return result
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())  # 세로, 가로
#
#     arr = [input() for _ in range(N)]
#     print('#{} {}'.format(tc, get_code(N, M)))