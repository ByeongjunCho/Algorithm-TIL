# def freedom(k, N, cnt, day):
#     global result
#     for i in range(k+day, N):
#         freedom(i, N, cnt + P[i], T[i])
#         print(cnt)
#         result = max(cnt, result)
#
# N = int(input())
# T = []
# P = []
# for _ in range(N):
#     d, p = map(int, input().split())
#     T.append(d)
#     P.append(p)
#
#
# for i in range(N-1, -1, -1):
#     if T[i] + i > N:
#         T.pop()
#         P.pop()
#     else:
#         break
#
#
# result = 0
# freedom(0, len(T), 0, 0)
# print(result)


# def freedom(k, N, cnt, day):
#     global result
#     if k == N:
#         result = max(cnt, result)
#         return
#     day -= 1
#     for i in range(k, N):
#         if day > 0:
#             day -= 1
#             continue
#         freedom(i+1, N, cnt + P[i], T[i])
#
#
# N = int(input())
# T = []
# P = []
# for _ in range(N):
#     d, p = map(int, input().split())
#     T.append(d)
#     P.append(p)
#
# for i in range(N-1, -1, -1):
#     if T[i] + i > N:
#         T.pop()
#         P.pop()
#     else:
#         break
# result = 0
# freedom(0, len(T), 0, 0)
# print(result)




# def freedom(k, start, cnt, N):
#     global result
#     result = max(cnt, result)
#
#     for i in range(start, N):
#         if i+T[i] > N:
#             continue
#         freedom(k+1, i+T[i], cnt + P[i], N)
#
#
# N = int(input())
# T = []
# P = []
# for _ in range(N):
#     d, p = map(int, input().split())
#     T.append(d)
#     P.append(p)
#
# result = 0
# freedom(0, 0, 0, N)
# print(result)

N = int(input())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
def backtrack(day, p):  # day: 결정할 일, p: 지금까지 이익

    if day > N+1: return
    if day == N+1:
        global ans
        ans = max(ans, p)
        return
    # 상담을 하는 경우
    backtrack(day + arr[day][0], p + arr[day][1])
    # 상담을 하지 않는 경우
    backtrack(day+1, p)

backtrack(1, 0)
print(ans)