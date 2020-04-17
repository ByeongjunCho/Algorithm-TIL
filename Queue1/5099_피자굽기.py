# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza = deque(pizza)
    cook = deque()
    i = 0
    while pizza or cook:
        if i < N:
            for _ in range(N):
                cook.append([i, pizza.popleft()])
                i += 1
        if i < M:
            for _ in range(N):
                tmp = cook.popleft()
                tmp[1] = tmp[1] // 2
                if tmp[1]:
                    cook.append(tmp)
                else:
                    # if i < M:
                    if pizza:
                        cook.append([i, pizza.popleft()])
                        i += 1
        else:
            # for _ in range(N):
            #     tmp = cook.popleft()
            #     if tmp[0] == -1:
            #         pass
            #     else:
            #         cook.append(tmp)

            for _ in range(len(cook)):
                if len(cook) != 1:
                    tmp = cook.popleft()
                    tmp[1] = tmp[1] // 2
                    if tmp[1]:
                        cook.append(tmp)
                    else:
                        pass
                else:
                    tmp = cook.popleft()
                    result = tmp[0]

    print('#{} {}'.format(tc, result+1))












