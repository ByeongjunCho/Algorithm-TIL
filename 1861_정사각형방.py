# 1861. 정사각형 방

def usedfs():
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    def dfs(y, x, cnt):
        visit[y][x] = 1
        tempmax[0] = max(tempmax[0], cnt)
        for i in range(4):
            wy, wx = y+dy[i], x+dx[i]
            if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == arr[y][x] + 1:
                visit[wy][wx] = 1
                dfs(wy, wx, cnt+1)

    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        maxVal = 0 # 최대값을 알기 위한 임시변수
        minVec = [0] * (N*N+1) # 최대값중 가장 작은 행렬값을 알기 위한 벡터
        visit = [[0 for _ in range(N)] for _ in range(N)]  # 방문 기록

        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    tempmax = [0]  # dfs를 돌리면서 얻을 수 있는 최대방문 기록
                    dfs(i, j, 1)
                    # 최대값 저장
                    if tempmax[0] > maxVal:
                        maxVal = tempmax[0]
                        minVec[arr[i][j]] = tempmax[0]

        # 함수가 끝나면 최대값중 가장 작은 value를 출력
        print("#{} {} {}".format(tc, minVec.index(maxVal), maxVal))

def usebfs():
    from collections import deque
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(y, x):
        Q = deque()
        Q.append((y, x))

        while Q:
            y, x = Q.popleft()
            for i in range(4):
                wy, wx = y+dy[i], x+dx[i]
                if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == arr[y][x] + 1:
                    D[wy][wx] = D[y][x] + 1
                    tempmax[0] = max(tempmax[0], D[wy][wx])
                    Q.append((wy, wx))

    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        maxVal = 0  # 최대값을 알기 위한 임시변수
        minVec = [0] * (N * N + 1)  # 최대값중 가장 작은 행렬값을 알기 위한 벡터
        D = [[0 for _ in range(N)] for _ in range(N)]  # 거리

        for i in range(N):
            for j in range(N):
                if not D[i][j]:
                    tempmax = [0]  # bfs를 돌리면서 얻을 수 있는 최대방문 기록
                    bfs(i, j)
                    # 최대값 저장
                    if tempmax[0] >= maxVal:
                        maxVal = tempmax[0]
                        minVec[arr[i][j]] = tempmax[0]

        # 함수가 끝나면 최대값중 가장 작은 value를 출력
        print("#{} {} {}".format(tc, minVec.index(maxVal), maxVal+1))

def useVec():
    def getVisit(y, x):
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]
        for i in range(4):
            wy, wx = dy[i] + y, dx[i] + x
            if 0 <= wy < N and 0 <= wx < N and arr[wy][wx] == arr[y][x] + 1:
                visit[arr[y][x]] = 1
                return 0

    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        visit = [0 for _ in range(N*N+1)]

        for i in range(N):
            for j in range(N):
                getVisit(i, j)
        # visit함수를 탐색하면서 1이 연속적으로 가장 많은 구간을 확인한다.
        sidx = 0 # 시작 인덱스
        idx = 0 # 위치 인덱스
        myVal = 0 # 최대 이동거리
        myIdx = 0 # 최대 이동거리 시작 인덱스
        cnt = 0 # 이동거리를 구하기 위한 변수
        while idx < N*N+1:
            # 현재 위치에 1이 있다면
            if visit[idx]:
                if cnt == 0:
                    sidx = idx  # cnt가 0이라면 시작 인덱스이다
                idx += 1
                cnt += 1
            else:
                # 현재 위치가 0이 되면
                if cnt > myVal:  # 최대값인지 확인하여
                    myVal = cnt
                    myIdx = sidx
                idx += 1
                sidx = idx
                cnt = 0

        # 함수가 끝나면 최대값중 가장 작은 value를 출력
        print("#{} {} {}".format(tc, myIdx, myVal+1))

useVec()