T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    box = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    box.sort(reverse=True)
    truck.sort(reverse=True)
    i, j, weight = 0, 0, 0  # box idx, truck idx, weight
    while i < N and j < M:
        if box[i] <= truck[j]:
            weight += box[i]
            i += 1
            j += 1
        # elif box[i] > truck[j]:
        #     i += 1
        else:
            i += 1
    print('#{} {}'.format(tc, weight))



