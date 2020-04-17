G = [[], [2,3,4], [5], [], [6], [], []]
value = [0, 30, 54, 2, 45, 1, 123]
k = 0
def dfs(n, k):
    if k == 0:
        print(value[n], end=' ')
    else:
        print('-------', value[n], end=' ')
    for v in G[n]:
        dfs(v, k+1)
    print()

dfs(1, 0)