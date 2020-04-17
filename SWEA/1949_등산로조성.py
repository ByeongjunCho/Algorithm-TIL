# # 1949. [모의 SW 역량테스트] 등산로 조성
# dy = (0, 0, 1, -1)
# dx = (1, -1, 0, 0)
# def dfs(v, val, cnt):
#     if val == MAX:
#         global result
#         result = max(result, cnt)
#         return
#
#     for i in range(4):
#         wy = dy[i] + v[0]
#         wx = dx[i] + v[1]
#         if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] > val and not visit[wy][wx]:
#             visit[wy][wx] = 1
#             dfs((wy, wx), arr[wy][wx], cnt+1)
#             visit[wy][wx] = 0
#
#
# for tc in range(1, int(input()) + 1):
#     N, K = map(int, input().split())   # 행렬 크기, 깎을 수 있는 높이
#     visit = [[0 for _ in range(N)] for _ in range(N)]
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     MAX = 0
#     MAX_count = 0
#     for a in arr:
#         MAX = max(MAX, max(a))
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == MAX:
#                 MAX_count += 1
#
#     result = 0
#     # 공사없이 수행
#     for i in range(N):
#         for j in range(N):
#             visit[i][j] = 1
#             dfs((i, j), arr[i][j], 1)
#             visit = [[0 for _ in range(N)] for _ in range(N)]
#
#     for deep in range(1, K+1):
#         # 공사 후 수행
#         for r in range(N):
#             for c in range(N):
#                 # MAX값이 하나뿐이라면, MAX - K를 수행하고
#                 if arr[r][c] == MAX and MAX_count == 1:
#                     tmpMAX = MAX
#                     arr[r][c] -= deep
#                     # 다시 MAX값을 찾아서 갱신한다.
#                     for a in arr:
#                         MAX = max(MAX, max(a))
#                     # 그리고 dfs를 수행한다.
#                     for i in range(N):
#                         for j in range(N):
#                             visit[i][j] = 1
#                             dfs((i, j), arr[i][j], 1)
#                             visit = [[0 for _ in range(N)] for _ in range(N)]
#                     # 다시 MAX를 복구해준다.
#                     arr[r][c] += deep
#                     MAX = tmpMAX
#                 else:
#                     arr[r][c] -= deep
#                     for i in range(N):
#                         for j in range(N):
#                             visit[i][j] = 1
#                             dfs((i, j), arr[i][j], 1)
#                             visit = [[0 for _ in range(N)] for _ in range(N)]
#                     arr[r][c] += deep
#
#
#     print('#{} {}'.format(tc, result))



# 1949. [모의 SW 역량테스트] 등산로 조성
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
def dfs(v, val, cnt, dig):
    if val == MAX:
        global result
        result = max(result, cnt)
        return

    for i in range(4):
        wy = dy[i] + v[0]
        wx = dx[i] + v[1]
        if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] > val and not visit[wy][wx]:
            visit[wy][wx] = 1
            dfs((wy, wx), arr[wy][wx], cnt+1)
            visit[wy][wx] = 0


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())   # 행렬 크기, 깎을 수 있는 높이
    visit = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
