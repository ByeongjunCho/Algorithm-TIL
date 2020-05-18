# SWEA 5648_원자 소멸 시뮬레이션

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atom = dict()
    for _ in range(N):
        # x위치, y위치, 이동방향 0123 상하좌우 k 에너지
        x, y, z, k = map(int, input().split())
        atom[(x, y)] = (z, k)

    result = 0
    # 0.5씩 이동
    # 원자는 (-1000, 1000)범위에 있고 0.5씩 이동하도록 설정했으므로 최대 이동은 4천번이다.
    for _ in range(4010):
        # 원자들이 없으면 할 필요가 없어진다.
        if not atom:
            break
        atom_items = list(atom.items())
        # atom의 key와 val을 담았으니 필요가 없다.
        atom.clear()

        # 충돌한 원자들을 담는 그릇
        tmp = dict()

        for (x, y), (z, k) in atom_items:
            if z == 0:
                x, y = x, y+0.5
            elif z == 1:
                x, y = x, y-0.5
            elif z == 2:
                x, y = x-0.5, y
            else:
                x, y = x+0.5, y

            # 범위를 넘어가면 밑에 계산을 해줄 필요가 없다.
            if not (-1000 <= x <= 1000 and -1000 <= y <= 1000):
                continue
            # atom dict에 충돌하는 원자가 존재하면 임시 dict에 저장
            if atom.get((x, y)):
                _, tmp_k = atom.pop((x, y))
                tmp[(x, y)] = (k+tmp_k)

            # tmp dict에 충돌하는 원자가 존재하면
            elif tmp.get((x, y)):
                tmp[(x, y)] = tmp[(x, y)] + k

            # 그렇지 않다면 atom에 입력
            else:
                atom[(x, y)] = (z, k)

        # 사이클이 끝날 때마다 tmp에 있는 원자 에너지 값을 저장한다.
        result += sum(tmp.values())


    # 해당 사이클이 끝나면 결과를 출력한다.
    print("#{} {}".format(tc, result))