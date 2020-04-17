from copy import deepcopy
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
copy_arr = deepcopy(arr)


def kill(arr, col, d, height):  # 행렬, 위치, 거리
    k = 0

    while k < d:
        start = [height-1, col-k]   # 시작점
        end = [height-1, col+k]  # 끝나는 점
        center = [height-k-1, col]
        # start에서 오른쪽 위로 올라감
        while True:
            y, x = start[0], start[1]
            if 0 <= y < height and 0 <= x < M and arr[y][x]:
                return (y, x)

            start = [start[0] - 1, start[1] + 1]
            if start[0] < center[0]:
                break
        # center에서 오른쪽 아래로
        start = center
        while True:
            y, x = start[0], start[1]
            if 0 <= y < height and 0 <= x < M and arr[y][x]:
                return (y, x)

            start = [start[0] + 1, start[1] + 1]
            if start[0] > end[0]:
                break
        k += 1


s = []
def comb(k):
    if len(s) == 3:
        global result
        height = N
        copyarr = deepcopy(arr)
        count = 0
        while copyarr:
            k = set()
            for col in s:
                xy = kill(copyarr, col, D, height)
                if xy:
                    k.add(xy)  # 각 궁수 위치에서 죽일 수 있는 군인의 좌표를 출력
            # 좌표에 있는 군인 제거
            for i in k:
                copyarr[i[0]][i[1]] = 0
            count += len(k)
            copyarr.pop()
            height -= 1
        result = max(result, count)
        return

    for i in range(k, M):
        s.append(i)
        comb(i+1)
        s.pop()

result = 0


comb(0)
print(result)