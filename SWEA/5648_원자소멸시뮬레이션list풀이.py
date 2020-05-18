# SWEA 5648_원자 소멸 시뮬레이션

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atom = []
    for _ in range(N):
        # x위치, y위치, 이동방향 0123 상하좌우 k 에너지
        x, y, z, k = map(int, input().split())
        x = (x+1000) * 2
        y = (y+1000) * 2
        atom.append([y, x, z, k])  # 배열 인덱스는 y,x 순이니까 바꿔서 수행
    # 충돌 확인용 배열을 만들어 놓는다.
    # 이 배열 밖에서는 충돌할 수 없을 것이다. 중간에 방향이 변하지 않을 것이기 때문에
    arr = [[[0, 0, 0] for _ in range(4005)] for _ in range(4005)]  # y, x: 행렬의 인덱스, [방향, 에너지, 출돌횟수]
    result = 0
    # 0.5씩 이동
    # 원자는 (-1000, 1000)범위에 있고 0.5씩 이동하도록 설정했으므로 최대 이동은 4천번이다.
    for _ in range(4010):
        # 원자들이 없으면 할 필요가 없어진다.
        if not atom:
            break

        # 원자가 있는 좌표를 저장하는 배열을 만든다.
        tmp = []
        while atom:
            y, x, z, k = atom.pop()
            if z == 0:
                x, y = x, y+1
            elif z == 1:
                x, y = x, y-1
            elif z == 2:
                x, y = x-1, y
            else:
                x, y = x+1, y

            # 이동한 원자를 배열에 저장하고 임시 배열에 좌표를 저장한다.
            if 0 <= x <= 4004 and 0 <= y <= 4004:
                # arr[y][x] = [방향, 에너지, 출돌횟수]
                # 방향은 중첩에서 넣어도 문제가 없다. (충돌이 1이상이면 제거할꺼라서)
                arr[y][x][0], arr[y][x][1], arr[y][x][2] = z, arr[y][x][1] + k, arr[y][x][2] + 1
                tmp.append([y, x])

        # tmp에 있는 좌표를 꺼내서
        while tmp:
            y, x = tmp.pop()
            # 충돌이 1보다 크면
            z, k, crash = arr[y][x]
            if crash > 1:
                result += k
                # 초기화
                arr[y][x] = [0, 0, 0]
            # 충돌이 1이면
            else:
                atom.append([y, x, z, k])
                arr[y][x] = [0, 0, 0]

    # 해당 사이클이 끝나면 결과를 출력한다.
    print("#{} {}".format(tc, result))