def check_win(arr1, arr2):
    # 1. run 체크
    for i in range(8):
        if arr1[i] and arr1[i + 1] and arr1[i + 2]:
            return 1
    # 2. triplet 체크
    if max(arr1) >= 3:
        return 1

    for i in range(8):
        if arr2[i] and arr2[i + 1] and arr2[i + 2]:
            return 2
    if max(arr2) >= 3:
        return 2
    return 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    result = 0
    for i in range(0, 12, 2):

        p1[card[i]] += 1
        p2[card[i+1]] += 1
        result = check_win(p1, p2)
        if result:
            break
    print('#{} {}'.format(tc, result))