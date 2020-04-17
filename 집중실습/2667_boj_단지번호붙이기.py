# from collections import deque
# N = int(input())
# arr = [list(map(int, list(input()))) for _ in range(N)]
# visit = [[0 for _ in range(N)] for _ in range(N)]
#
# def BFS(v, num):
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     Q = deque([v])
#     while Q:
#         v = Q.popleft()
#         visit[v[0]][v[1]] = num
#         for i in range(4):
#             wy, wx = v[0] + dy[i], v[1] + dx[i]
#             if 0 <= wy < N and 0 <= wx < N and not visit[wy][wx] and arr[wy][wx]:
#                 # arr[wy][wx] = num
#                 Q.append([wy, wx])
#
# danji = 1
# for i in range(N):
#     for j in range(N):
#         if not visit[i][j] and arr[i][j]:
#             BFS([i,j], danji)
#             danji += 1
#
# print(danji-1)
# S = [0] * (danji-1)
# for vals in visit:
#     for i in range(1, danji):
#         S[i-1] += vals.count(i)
#
# S.sort()
# for i in range(len(S)):
#     print(S[i])



N = int(input())
visit = [[0 for _ in range(N)] for _ in range(N)]
arr = [list(map(int, input())) for _ in range(N)]
G = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def DFS(v, k):
    visit[v[0]][v[1]] = True
    arr[v[0]][v[1]] = k
    for w in G:
        if 0 <= v[0] + w[0] <= N-1 and 0 <= v[1] + w[1] <= N-1 and not visit[v[0] + w[0]][v[1] + w[1]] and arr[v[0] + w[0]][v[1] + w[1]]:
            w = [v[0] + w[0], v[1] + w[1]]
            DFS(w, k)


mark = 1
for row in range(N):
    for col in range(N):
        if not visit[row][col] and arr[row][col]:
            DFS([row, col], mark)
            mark += 1

status = [0] * mark
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            status[arr[i][j]] += 1

status.sort()
print(mark-1)
for i in range(1, mark):
    print(status[i])