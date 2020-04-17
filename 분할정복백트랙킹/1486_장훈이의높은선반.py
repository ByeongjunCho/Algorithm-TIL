def top(k, start, used, height):
    global N, B, result
    if height > result:
        return
    if height >= B:
        result = min(result, height)
        return
    if k > N:
        return

    for i in range(start, -1, -1):
        if used & (1 << i):
            continue
        else:
            top(k+1, i, used | (1 << i), height + slave[i])
            top(k+1, i, used, height)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())  # 점원의 수, 탑의 높이
    slave = list(map(int, input().split()))
    # greedy 를 이용해 최적의 값을 찾아본다.
    slave.sort()
    greedy_height = 0
    for i in range(N):
        greedy_height += slave[i]
        if greedy_height >= B:
            break
    # 반복되는 횟수 저장(i보다 작거나 같은 반복수가 최적의 결과값이 될 것이다.)
    result = greedy_height
    height = 0
    top(0, N-1, 0, 0)
    print('#{} {}'.format(tc, result - B))

