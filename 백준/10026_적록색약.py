# def BFS_RGB(start):
#     Q = deque()
#     Q.append(start)
#     visit[start[0]][start[1]] = 1
#     mode = arr[start[0]][start[1]]
#     while Q:
#         v = Q.popleft()
#         for i in range(4):
#             wy, wx = dy[i] + v[0], dx[i] + v[1]
#             if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == mode and not visit[wy][wx]:
#                 visit[wy][wx] = 1
#                 Q.append((wy, wx))
#
#
# def BFS_RB(start):
#     Q = deque()
#     Q.append(start)
#     visit[start[0]][start[1]] = 1
#     mode = arr[start[0]][start[1]]
#
#     if mode == 'R' or mode == 'G':
#         while Q:
#             v = Q.popleft()
#             for i in range(4):
#                 wy, wx = dy[i] + v[0], dx[i] + v[1]
#                 if 0 <= wy < N and 0 <= wx < N and (arr[wy][wx] == 'R' or arr[wy][wx] == 'G') and not visit[wy][wx]:
#                     visit[wy][wx] = 1
#                     Q.append((wy, wx))
#     else:
#         while Q:
#             v = Q.popleft()
#             for i in range(4):
#                 wy, wx = dy[i] + v[0], dx[i] + v[1]
#                 if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == mode and not visit[wy][wx]:
#                     visit[wy][wx] = 1
#                     Q.append((wy, wx))
#
# RGB = 0
# for i in range(N):
#     for j in range(N):
#         if not visit[i][j]:
#             BFS_RGB((i, j))
#             RGB += 1
#
# # visit 행렬 초기화
# visit = [[0 for _ in range(N)] for _ in range(N)]
#
# RB = 0
# for i in range(N):
#     for j in range(N):
#         if not visit[i][j]:
#             BFS_RB((i, j))
#             RB += 1
#
# print('{} {}'.format(RGB, RB))

import sys
sys.setrecursionlimit(100000)

N = int(input())
arr = [input() for _ in range(N)]

visit_RGB = [[0 for _ in range(N)] for _ in range(N)]
visit_RB = [[0 for _ in range(N)] for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def dfs(start, mode):
    if mode == 'RGB':
        visit_RGB[start[0]][start[1]] = 1
        for i in range(4):
            wy, wx = start[0] + dy[i], start[1] + dx[i]
            if 0 <= wy < N and 0 <= wx < N and arr[wy][wx]==arr[start[0]][start[1]] and not visit_RGB[wy][wx]:
                dfs((wy, wx), mode)
    else:
        visit_RB[start[0]][start[1]] = 1
        if arr[start[0]][start[1]] == 'B':
            for i in range(4):
                wy, wx = start[0] + dy[i], start[1] + dx[i]
                if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == 'B' and not visit_RB[wy][wx]:
                    dfs((wy, wx), mode)
        else:
            for i in range(4):
                wy, wx = start[0] + dy[i], start[1] + dx[i]
                if 0 <= wy < N and 0 <= wx < N and (arr[wy][wx] == 'R' or arr[wy][wx] == 'G') and not visit_RB[wy][wx]:
                    dfs((wy, wx), mode)

RGB = 0
RB = 0
for i in range(N):
    for j in range(N):
        if not visit_RGB[i][j]:
            dfs((i, j), 'RGB')
            RGB += 1
        if not visit_RB[i][j]:
            dfs((i, j), 'RB')
            RB += 1

print('{} {}'.format(RGB, RB))