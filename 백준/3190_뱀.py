from collections import deque
N = int(input())
K = int(input()) # 사과의 수
arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 3 # 사과

snake = deque()
snake.append([0, 0])
def go(status): # 0123
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # head 추출
    i, j = snake[0]
    wy = i + dy[status]
    wx = j + dx[status]
    if 0 <= wy < N and 0 <= wx < N:
        if [wy, wx] in snake:
            return False
        else:
            snake.appendleft([wy, wx])
    else:
        return False
    # 머리에 사과가 없다면 꼬리 제거
    if arr[wy][wx] != 3:
        snake.pop()
    else:
        arr[wy][wx] = 0
    return True

L = int(input())
times = [0] * L
for i in range(L):
    t, s = input().split()
    times[i] = [int(t), s]

t = 1
index = 0
s = 1
while go(s):
    if index < L:
        if times[index][0] == t:
            if times[index][1] == 'L':
                s -= 1
            else:
                s += 1
            index += 1

    if s>3:
        s = 0
    elif s<0:
        s = 3
    t += 1

print(t)