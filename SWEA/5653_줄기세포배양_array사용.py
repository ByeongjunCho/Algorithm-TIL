# 5653. [모의 SW 역량테스트] 줄기세포배양

for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())  # 행, 열, 시간
    tmp = [list(map(int, input().split())) for _ in range(N)]

    # 모든 정보가 담긴 행렬을 만든다.
    # [생명력, 활성화 카운트, 현재 시간]
    arr = [[[0, 0, 0] for _ in range(350)] for _ in range(350)]

    # 확인해야 할 세포 리스트 생성
    check = set()

    for i in range(N):
        for j in range(M):
            val = tmp[i][j]
            if val:
                arr[i+160][j+160] = [val, -val, 0]
                # check.append([i+300, j+300])
                check.update([(i+160, j+160)])

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    for t in range(K):
        if not check:
            break
        # 임시로 다음 상태에 체크할 좌표를 저장할 행렬
        tmp = list(check)
        check.clear()
        for y, x in tmp:
            # [생명력, 활성화 카운트, 현재 시간]
            life, lifecnt, cnt = arr[y][x]

            # 1. 만약 활성화되지 않은 것이라면
            if life and lifecnt < 0 and cnt == t:
                arr[y][x] = [life, lifecnt+1, t+1]  # 해당 세포에 다음상태를 입력
                check.update([(y, x)])

            # 2. 복사할 수 있는 상태가 되면
            elif life and 0 <= lifecnt < life and cnt == t:
                # 주변 확인
                for i in range(4):
                    wy, wx = y+dy[i], x+dx[i]
                    w_life, w_lifecnt, w_cnt = arr[wy][wx]
                    # 2.1 비어있으면
                    if arr[wy][wx] == [0, 0, 0]:
                        arr[wy][wx] = [life, -life, t+1]
                        # tmp.append([wy, wx])
                        check.update([(wy, wx)])
                    # 2.2 금방 복사된 세포라면
                    elif w_life == -w_lifecnt and w_cnt == t+1:
                        # 현재 세포의 생명력과 비교해서
                        if life > w_life:
                            # 갱신
                            arr[wy][wx] = [life, -life, t+1]


                # 주변 작업을 끝내고 현재값 갱신
                arr[y][x] = [life, lifecnt+1, t+1]

                # # 해당 세포가 죽었다면 check에 넣을 필요가 없음
                if lifecnt+1 < life:
                    # tmp.append([y, x])
                    check.update([(y, x)])

    print("#{} {}".format(tc, len(check)))
