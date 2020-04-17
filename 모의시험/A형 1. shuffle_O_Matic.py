

def shuffle_card(arr, x):
    half_N = len(arr) >> 1
    left = range(half_N, 0, -1)
    right = range(1, half_N+1)
    if x < half_N:
        status = 0
    else:
        x -= half_N
        status = 1
    i = j = 0
    S = []
    while i != half_N or j != half_N:
        if not status:
            for _ in range(left[x]):
                if i == half_N:
                    break
                S.append(arr[i])
                i += 1
            S.append(arr[j+half_N])
            j += 1
        else:
            for _ in range(right[x]):
                if j == half_N:
                    break
                S.append(arr[j+half_N])
                j += 1
            S.append(arr[i])
            i += 1
    return S

def shuffle_O(arr, cnt, N):
    if cnt > 5 or cnt > result[0]:
        return
    if arr1 == arr or arr2 == arr:  # 최소값저장이 필요
        result[0] = min(result[0], cnt)
        return

    for i in range(1, N):
        # if i == k:
        #     continue
        shuffle = shuffle_card(arr, i)
        shuffle_O(shuffle, cnt+1, N)



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    case = list(map(int, input().split()))
    arr1 = sorted(case)
    arr2 = list(reversed(arr1))
    result = [9999]
    shuffle_O(case, 0, N)
    print("#%d %d" % (test_case, result[0]))

