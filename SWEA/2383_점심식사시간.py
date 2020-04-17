# 2383. [모의 SW 역량테스트] 점심 식사시간

for tc in range(1, 1+int(input())):
    peoples = []
    lunch = []
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:  # 사람위치
                peoples.append([i, j])
            elif tmp[j] > 1: # 계단위치
                lunch.append([i, j, tmp[j]]) # 계단 길이 추가
            arr[i][j] = tmp[j]

    # 사람이 각각 계단으로 가는 거리를 저장
    people_lunch1 = [abs(lunch[0][0] - row) + abs(lunch[0][1] - col) for row, col in peoples]
    people_lunch2 = [abs(lunch[1][0] - row) + abs(lunch[1][1] - col) for row, col in peoples]

    st1 = [0] * lunch[0][2] # 계단1
    st2 = [0] * lunch[1][2] # 계단2

    def simul(go1, go2):  # 1분이 지난 후 상태 (go1과 go2는 정렬된 상태)
        for i in range(len(go1)):
            go1[i] -= 1

        for i in range(len(go2)):
            go2[i] -= 1

        # 각 계단에 있는 사람을 한칸씩 앞으로
        if st1[-1]:
            st1[-1] = 0
        for i in range(len(st1)-1, 0, -1):
            st1[i] = st1[i-1]
            st1[i-1] = 0

        if st2[-1]:
            st2[-1] = 0
        for i in range(len(st2)-1, 0, -1):
            st2[i] = st2[i-1]
            st2[i-1] = 0

        while go1 and go1[-1] <= -1 and sum(st1) < 3:
            st1[0] += 1
            go1.pop()

        while go2 and go2[-1] <= -1 and sum(st2) < 3:
            st2[0] += 1
            go2.pop()

    s = []
    go1 = []
    go2 = []
    result = 0xffffff
    def comb(start):
        global result
        for i in range(len(people_lunch1)):
            if i in s:
                go1.append(people_lunch1[i])
            else:
                go2.append(people_lunch2[i])
        count = 0
        stats = 0
        go1.sort(reverse=True)
        go2.sort(reverse=True)

        while go1 or go2 or sum(st1) or sum(st2):
            simul(go1, go2)
            count += 1
            if count > result:
                stats = 1
                break
        if not stats:
            result = min(result, count)

        # 계단 초기화
        for i in range(len(st1)):
            st1[i] = 0
        for i in range(len(st2)):
            st2[i] = 0

        go1.clear()
        go2.clear()

        for i in range(start, len(people_lunch1)):
            s.append(i)
            comb(i+1)
            s.pop()

    comb(0)
    print('#{} {}'.format(tc, result))