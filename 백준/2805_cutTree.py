N, M = map(int, input().split())
tree = list(map(int, input().split()))

# def sangen(tree, N, M):
#     for val in range(max(tree)-1, -1, -1):
#         sangen_tree = 0
#         for j in range(N):
#             sangen_tree += tree[j]-val if tree[j] > val else 0
#         if sangen_tree >= M:
#             return val

# print(sangen(tree, N, M))


N, M = map(int, input().split())
tree = list(map(int, input().split()))

