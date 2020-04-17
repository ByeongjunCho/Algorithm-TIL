result = 0
def get_node(v):
    global result
    result += 1
    if v == 0:
        result -= 1
        return
    get_node(tree[0][v])
    get_node(tree[1][v])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0 for _ in range(E+2)] for _ in range(2)]
    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp), 2):
        if not tree[0][tmp[i]]:
            tree[0][tmp[i]] = tmp[i+1]
        else:
            tree[1][tmp[i]] = tmp[i + 1]
    get_node(N)
    print('#{} {}'.format(tc, result))
    result = 0

