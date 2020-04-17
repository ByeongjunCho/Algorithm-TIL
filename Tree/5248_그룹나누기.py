def find_set(x):
    if root[x] != x:
        root[x] = find_set(root[x])
    return root[x]

def Union_set(x, y):
    root[find_set(y)] = find_set(x)
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    root = [x for x in range(N+1)]
    numbers = list(map(int, input().split()))
    # 부모 변경
    for i in range(M):
        # 싸이클 확인
        a = find_set(numbers[2 * i + 1])
        b = find_set(numbers[2*i])
        if a != b:
            Union_set(numbers[2 * i + 1], numbers[2*i])
    # 각 정점의 부모를 조상으로 변경
    for k in range(0, N+1):
        find_set(k)
    print('#{} {}'.format(tc, len(set(root)) - 1))