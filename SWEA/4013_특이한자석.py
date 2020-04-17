# 4013. [모의 SW 역량테스트] 특이한 자석
from collections import deque

def turn(tire, clockwise):  # 1: 시계방향 0: 반시계방향
    if clockwise == 1:
        tmp = tire.pop()
        tire.appendleft(tmp)
    elif clockwise == -1:
        tmp = tire.popleft()
        tire.append(tmp)



for tc in range(1, 1+int(input())):
    K = int(input())
    t1 = deque(list(map(int, input().split())))
    t2 = deque(list(map(int, input().split())))
    t3 = deque(list(map(int, input().split())))
    t4 = deque(list(map(int, input().split())))

    # 오른쪽 idx: 2 왼쪽 idx: 6
    tires = [0, t1, t2, t3, t4]
    for _ in range(K):
        num, clockwise = map(int, input().split())
        status = [0, 0, 0, 0, 0]
        status[num] = clockwise
        tmp = num
        for i in range(num, 4):
            if tires[i][2] != tires[i+1][6]:
                status[i+1] = -status[i]

        for j in range(num, 1, -1):
            if tires[j][6] != tires[j-1][2]:
                status[j-1] = -status[j]

        for i in range(1, 5):
            turn(tires[i], status[i])

    result = 0
    for i in range(1, 5):
        if tires[i][0] == 1:
            result += 2 ** (i-1)

    print('#{} {}'.format(tc, result))