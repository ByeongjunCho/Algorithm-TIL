# 1. 카메라들의 좌표와 종류를 저장
# 2. 하나씩 모드를 변경하면서 풀이
# 카메라종류 = [[[0]],
#          [[0], [1], [2], [3]],
#          [[0, 2], [3, 4]],
#          ....
#          ]


# 카메라 위치의 벽이 아닌 모든곳을 감시한다.
c = [1,2,3,4,5]
def camera1(arr, xy, status):
    if status == 1:
        # 1번 오른쪽
        w = xy[1]+1
        while w < M:
            if arr[xy[0]][w] == 0:
                arr[xy[0]][w] = '#'
            elif arr[xy[0]][w] == 6:
                break
            w += 1
    elif status == 2:
        # 1번 왼쪽
        w = xy[1] - 1
        while w >= 0:
            if arr[xy[0]][w] == 0:
                arr[xy[0]][w] = '#'
            elif arr[xy[0]][w] == 6:
                break
            w -= 1
    elif status == 3:
        # 1번 위
        w = xy[0] - 1
        while w >= 0:
            if arr[w][xy[1]] == 0:
                arr[w][xy[1]] = '#'
            elif arr[w][xy[1]] == 6:
                break
            w -= 1
    elif status == 4:
        # 1번 아래
        w = xy[0] + 1
        while w < N:
            if arr[w][xy[1]] == 0:
                arr[w][xy[1]] = '#'
            elif arr[w][xy[1]] == 6:
                break
            w += 1

def camera2(arr, xy, status):
    if status == 1 or status == 3:
        # 좌우
        camera1(arr, xy, 1)
        camera1(arr, xy, 2)
    elif status == 2 or status == 4:
        # 위아래
        camera1(arr, xy, 3)
        camera1(arr, xy, 4)

def camera3(arr, xy, status):
    if status == 1:
        # 위오른쪽
        camera1(arr, xy, 3)
        camera1(arr, xy, 1)
    elif status == 2:
        #오른쪽아래
        camera1(arr, xy, 1)
        camera1(arr, xy, 4)
    elif status == 3:
        # 왼쪽아래
        camera1(arr, xy, 2)
        camera1(arr, xy, 4)
    elif status == 4:
        # 왼쪽위
        camera1(arr, xy, 2)
        camera1(arr, xy, 3)

def camera4(arr, xy, status):
    if status == 1:
        # 위오아
        camera1(arr, xy, 1)
        camera1(arr, xy, 3)
        camera1(arr, xy, 4)
    elif status == 2:
        # 위오왼
        camera1(arr, xy, 1)
        camera1(arr, xy, 2)
        camera1(arr, xy, 3)
    elif status == 3:
        # 왼오아
        camera1(arr, xy, 1)
        camera1(arr, xy, 2)
        camera1(arr, xy, 4)
    elif status == 4:
        # 왼위아
        camera1(arr, xy, 2)
        camera1(arr, xy, 3)
        camera1(arr, xy, 4)

def camera5(arr, xy, status):
    camera1(arr, xy, 1)
    camera1(arr, xy, 2)
    camera1(arr, xy, 3)
    camera1(arr, xy, 4)



N, M = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(N)]
camera = []
for i in range(N):
    for j in range(M):
        if original[i][j] in c:
            camera.append((original[i][j], i, j))
c_num = len(camera)

order = [0] * c_num
def check(k, cccn):
    if k == cccn:
        arr = [[0 for _ in range(M)] for _ in range(N)]
        # 배열 복사
        for i in range(N):
            for j in range(M):
                arr[i][j] = original[i][j]

        # 배열을 이용하여 사각지대 제거
        for i in range(cccn):
            if camera[i][0] == 1:
                camera1(arr, [camera[i][1], camera[i][2]], order[i])
            elif camera[i][0] == 2:
                camera2(arr, [camera[i][1], camera[i][2]], order[i])
            elif camera[i][0] == 3:
                camera3(arr, [camera[i][1], camera[i][2]], order[i])
            elif camera[i][0] == 4:
                camera4(arr, [camera[i][1], camera[i][2]], order[i])
            elif camera[i][0] == 5:
                camera5(arr, [camera[i][1], camera[i][2]], order[i])
        tmp = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    tmp += 1
        global result
        result = min(result, tmp)
        return
    for i in range(1, 5):
        order[k] = i
        check(k+1, cccn)

result = 64
if c_num == 0:
    tmp = 0
    for i in range(N):
        for j in range(M):
            if original[i][j] == 0:
                tmp += 1
    print(tmp)
else:
    check(0, c_num)
    print(result)