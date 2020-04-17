from collections import deque
# def BFS(arr, R, C):
#     start = [0, 0]
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, -1, 1]
#     visit = [0 for _ in range(C) for _ in range(R)]
#     D = [0 for _ in range(C) for _ in range(R)]
#     A = deque()
#     Q = deque()
#     Q.append(start)
#     while Q:
#         v = Q.popleft()
#         for i in range(len(dx)):
#             w = [v[0] + dx[i], v[1] + dy[i]]
#             if w[0] < R and w[1] < C and not visit[w[0]][w[1]]

# def DFS(arr, R, C):
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     visit = [[0 for _ in range(C)] for _ in range(R)]
#     v = [0, 0]
#     S = [v]
#     A = [arr[v[0]][v[1]]]
#     visit[v[0]][v[1]] = 1
#     mymax = 0
#     while S:
#         for i in range(len(dx)):
#             w = [v[0] + dx[i], v[1] + dy[i]]
#             if 0 <= w[0] < R and 0 <= w[1] < C and not visit[w[0]][w[1]] and arr[w[0]][w[1]] not in A:
#                 S.append(w)
#                 visit[w[0]][w[1]] = 1
#                 v = w
#                 A.append(arr[w[0]][w[1]])
#                 break
#         else:
#             visit[v[0]][v[1]] = 0
#             v = S.pop()
#             mymax = max(mymax, len(A))
#             A.pop()
#
#     return mymax
#
#
# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
# print(DFS(arr, R, C))



def DFS(y, x, arr, R, C):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit[y][x] = 1
    # A.append(arr[y][x])
    A.update(arr[y][x])
    global result
    result = max(result, len(A))

    if len(A) == 26:
        return

    for i in range(4):
        wy, wx = y + dy[i], x+dx[i]
        if -1 < wy < R and -1 < wx < C and not visit[wy][wx] and arr[wy][wx] not in A:
            # A.append(arr[wy][wx])
            # visit[wy][wx] = 1
            DFS(wy, wx, arr, R, C)
            visit[wy][wx] = 0
            A.pop()

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
result = 0
# A = [arr[0][0]]
A = set()
visit = [[0 for _ in range(C)] for _ in range(R)]
# visit[0][0] = 1
DFS(0, 0, arr, R, C)
print(result)