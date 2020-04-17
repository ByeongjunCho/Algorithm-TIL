# def find_matrix(arr, N):
#     S = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 S.append(i)
#                 S.append(j)
#
#                 for l in range(N):
#                     if i+l >= N:
#                         S.append(i+l-1)
#                         # S.append([i, j])
#                         # S.append([i+l-1,j])
#                         break
#                     elif not arr[i+l][j]:
#                         S.append(i + l - 1)
#                         # S.append([i, i+l-1])
#                         break
#                 for k in range(N):
#                     if j+k >= N:
#                         S.append(j+k-1)
#                         # S.append([i, j])
#                         # S.append([i, j+k-1])
#                         break
#                     elif not arr[i][j+k]:
#                         S.append(j + k - 1)
#                         # S.append([i, j])
#                         # S.append([i, j + k - 1])
#                         break
#
#                 for row in range(i, i+l):
#                     for col in range(j, j+k):
#                         arr[row][col] = 0
#     result = []
#     for i in range(0, len(S), 4):
#         result.append(((S[i+2]-S[i]+1) * (S[i+3]-S[i+1]+1), S[i+2]-S[i]+1, S[i+3]-S[i+1]+1))
#     result.sort()
#     tmp = [str(len(result))]
#     for c in result:
#         tmp.append(str(c[1]))
#         tmp.append(str(c[2]))
#     return tmp
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print('#{} {}'.format(tc, ' '.join(find_matrix(arr, N))))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []   # 튜플로 행과 열의 크기 저장

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue

            r, c = i, 0   # r, c = 행과 열
            while r < N and arr[r][j]:
                c = j
                while c < N and arr[r][c]:
                    arr[r][c] = 0
                    c += 1
                r += 1

            ans.append((r-i, c-j))   # 행의 크기, 열의 크기

    ans.sort(key= lambda a: (a[0] * a[1], a[0]))