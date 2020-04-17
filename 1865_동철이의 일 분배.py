# 1865. 동철이의 일 분배

# def work(k, n, vec, val):
#     global greedyMax
#     if k == n:
#         mymax[0] = max(mymax[0], val, greedyMax)
#         return
#     if val <= mymax[0] or val < greedyMax: # 1보다 작은 수들은 곱할수록 작아진다
#         return
#
#     for i in range(N):
#         if not vec[i]:
#             vec[i] = 1
#             work(k+1, n, vec, val * workTable[k][i])
#             vec[i] = 0
#
# for tc in range(1, 1 + int(input())):
#     N = int(input())
#     workTable = [list(map(lambda x: x/100, map(int, input().split()))) for _ in range(N)]
#     useVec = [0 for _ in range(N)]
#     mymax = [0.]
#
#     # greedy하게 임의의 max값을 구한다.
#     visit = [0 for _ in range(N)]
#     greedyMax = 1.
#     for vec in workTable:
#         copyvec = [x for x in vec] # 임시 벡터
#         while True:
#             # 최대값과 인덱스를 구한다.
#             tempmax = 0
#             tempidx = 0
#             for i in range(N):
#                 if copyvec[i] >= tempmax:
#                     tempmax = copyvec[i]
#                     tempidx = i
#             if not visit[tempidx]:
#                 greedyMax *= tempmax
#                 visit[tempidx] = 1
#                 break
#             else:
#                 copyvec[tempidx] = 0
#
#     work(0, N, useVec, 1.0)
#     # print("# {} {0.6f}".format(tc, mymax[0] * 100))
#     print("#%s %0.6f" % (tc, mymax[0] * 100))

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    workTable = [list(map(lambda x: x/100, map(int, input().split()))) for _ in range(N)]
    used = [0 for _ in range(N)] # 선택 열 표시
    mymax = [0]
    def perm(k, N, val):
        if val <= mymax[0]:
            return
        if k == N:
            mymax[0] = max(mymax[0], val)
            return
        for i in range(N):
            if used[i]:
                continue
            used[i] = 1
            perm(k+1,N, val*workTable[k][i])
            used[i] = 0

    perm(0, N, 1)
    print("#{} {:.6f}".format(tc, mymax[0] * 100))