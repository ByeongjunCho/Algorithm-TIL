# boj 17822 원판 돌리기
from collections import deque
N, M, T = map(int, input().split())  # 원판크기, 숫자, 회전수
target = [0] * N
for i in range(N):
    v = list(map(int, input().split()))
    q = deque(v)
    target[i] = q

# 원판 회전 함수
def go(x, d, k):  # 배수, 방향(0: 시계, 1: 반시계), 회전수
    # 1. 회전시킬 원판의 번호를 가져옴
    tmp = target[x-1]
    # 2. 원판을 k번 회전시킴(방향 설정 필요)
    # 2.1 반시계방향인 경우
    if d:
        for _ in range(k):
            head = tmp.popleft()
            tmp.append(head)
    else:
        # 2.2 시계방향인 경우
        for _ in range(k):
            tail = tmp.pop()
            tmp.appendleft(tail)
# 원판 인접 판별 함수
def inner():
    count = 0
    tmp = 0
    xy = set()
    for i in range(N):
        for j in range(M):
            # signal = 0 인경우 평균을 구하기 위해 모두 더한다.
            if 1 <= target[i][j] <= 1000:
                tmp += target[i][j]
                count += 1
                if j == 0:
                    if target[i][j] == target[i][1]:
                        xy.add((i, j))
                        xy.add((i, 1))
                    if target[i][j] == target[i][M-1]:
                        xy.add((i, j))
                        xy.add((i, M-1))
                elif j == M-1:
                    if target[i][j] == target[i][j-1]:
                        xy.add((i, j))
                        xy.add((i, j-1))
                    if target[i][j] == target[i][0]:
                        xy.add((i, j))
                        xy.add((i, 0))
                else:
                    if target[i][j] == target[i][j-1]:
                        xy.add((i, j))
                        xy.add((i, j-1))
                    if target[i][j] == target[i][j+1]:
                        xy.add((i, j))
                        xy.add((i, j+1))

                if i == 0:
                    if target[0][j] == target[1][j]:
                        xy.add((i, j))
                        xy.add((1, j))
                elif i == N-1:
                    if target[i][j] == target[i-1][j]:
                        xy.add((i, j))
                        xy.add((i-1, j))
                else:
                    if target[i][j] == target[i-1][j]:
                        xy.add((i, j))
                        xy.add((i-1, j))
                    if target[i][j] == target[i+1][j]:
                        xy.add((i, j))
                        xy.add((i+1, j))
    if xy:
        for i, j in xy:
            target[i][j] = 0
        return
    else:
        avg = tmp / count
        for i in range(N):
            for j in range(M):
                if 1 <= target[i][j] <= 1000:
                    if target[i][j] > avg:
                        target[i][j] -= 1
                    elif target[i][j] < avg:
                        target[i][j] += 1

for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(x, N+1, x):
        go(i, d, k)
    inner()

result = 0
for i in range(N):
    for j in range(M):
        result += target[i][j]

print(result)