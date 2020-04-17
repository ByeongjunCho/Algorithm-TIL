def bus2(k, start):
    global result
    if k > result:
        return
    if start == arr[0]:
        result = min(result, k)
        return
    for i in range(start + arr[start], start, -1):
        if i > arr[0]:
            continue
        bus2(k + 1, i)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 150
    bus2(-1, 1)

    print('#{} {}'.format(tc, result))