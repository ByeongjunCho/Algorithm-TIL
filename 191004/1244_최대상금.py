# num = [4,5,6,7,8,9]
# N = len(num)
# cnt = 10
# # 두 개의 숫자를 선택해서 교환
# # 교환횟수 1회 일때 => 5C2만큼 선택지
# visit = [[0] * 1000000 for _ in range(11)]
# MAX = 0
# def backtrack(k):
#     global MAX
#     val = int(''.join(map(str, num)))
#     if visit[k][val]:
#         return
#     visit[k][val] = 1
#     if k == cnt:
#         if val > MAX:
#             MAX = val
#         return
#     else:
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 num[i], num[j] = num[j], num[i]
#                 backtrack(k + 1)
#                 num[i], num[j] = num[j], num[i]
#
# backtrack(0)
# print(MAX)

# for i in range(N-1):
#     for j in range(i+1, N):
#         num[i], num[j] = num[j], num[i]
#         # ----------------
#         # 재귀호출 필요
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 num[i], num[j] = num[j], num[i]
#                 print(num)
#                 num[i], num[j] = num[j], num[i]
#         # ----------------
#         num[i], num[j] = num[j], num[i]


'''bfs를 이용한 방법'''
# import collections
# d = [1, 10, 100, 1000, 10000, 100000]
# def swap(val, i, j): # 정수 --> 교환된 결과인 정수
#     a = (val // d[i]) % 10
#     b = (val // d[j]) % 10
#     return val - a * d[i] + a * d[j] - b * d[j] + b * d[i]
#
# num = 32888
# N = len(num)
# cnt = 10
# # 두 개의 숫자를 선택해서 교환
# # 교환횟수 1회 일때 => 5C2만큼 선택지
# visit = [[0] * 1000000 for _ in range(11)]
# MAX = 0
# Q = collections.deque()
# Q.append((num, 0))  # 숫자, 교환횟수
#
# while Q:
#     val, k = Q.popleft()
#     if k == cnt:
#         MAX = max(MAX, val)
#     else:
#         for i in range(N - 1):
#             for j in range(i, N):
#                 t = swap(val, i, j)
#                 if visit[k][t] == 1: continue
#                 Q.append((t, k+1))
# print(MAX)

def swap(val, i, j):
    d = (1, 10, 100, 1000, 10000, 100000)
    a = (val // d[i]) % 10
    b = (val // d[j]) % 10
    return val - d[i] * a + d[j] * a - d[j] * b + d[i] * b

T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    N = len(num)
    num, cnt = int(num), int(cnt)
    cnt_arr = [set() for _ in range(cnt+1)]
    cnt_arr[0].add(int(num))
    for k in range(1, cnt+1):
        for l in cnt_arr[k-1]:
            for i in range(N-1):
                for j in range(i+1, N):
                    cnt_arr[k].add(swap(l, i, j))
    print('#{} {}'.format(tc, max(cnt_arr[-1])))




