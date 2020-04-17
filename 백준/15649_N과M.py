N, M = map(int, input().split())

# 수열
order = [0] * M
result = []

def perm(k, n, N, used):
    if k == n:
        result.append(order[:])
        return

    for i in range(1, N+1):
        if used & (1 << i): continue
        order[k] = i
        perm(k+1, n, N, used | (1 << i))


# def perm(k, n):
#     global N
#     if k == n:
#         result.append(order[:N+1])
#         # for j in range(n):
#         #     print(order[j], end=' ')
#         # print()
#         # return
#
#     for i in range(k, N):
#         order[k], order[i] = order[i], order[k]
#         perm(k+1, n)
#         order[i], order[k] = order[k], order[i]

perm(0, M, N, 0)

for i in range(len(result)):
    for j in range(M):
        if j != M-1:
            print(result[i][j], end=' ')
        else:
            print(result[i][j])
