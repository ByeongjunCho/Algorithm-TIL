def comb(k, start):
    if k == 2:
        global honey_tmp, result
        tmp = 0
        for i in honey[0]:
            if i in honey[1]:
                return
        # 전역변수 초기화
        honey_tmp = 0

        max_honey(0, honey[0], 0, 0)
        tmp += honey_tmp
        honey_tmp = 0
        max_honey(0, honey[1], 0, 0)
        tmp += honey_tmp
        result = max(result, tmp)
        return

    for i in range(start, len(idx)):
        honey[k] = idx[i]
        comb(k+1, i+1)

def max_honey(k, slave, val, val_sq):
    global C, honey_tmp
    if val > C:
        return

    if k == M:
        honey_tmp = max(honey_tmp, val_sq)
        return

    max_honey(k+1, slave, val + arr[slave[k][0]][slave[k][1]], val_sq + arr[slave[k][0]][slave[k][1]]**2)
    max_honey(k+1, slave, val, val_sq)


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())  # 배열 크기, 일꾼 채취범위, 채취 최대량
    arr = [list(map(int, input().split())) for _ in range(N)]
    honey = [0] * 2  # 조합값을 넣기 위한 임시 배열

    idx = []
    for i in range(N-M+1):
        for j in range(N):
            tmp = []
            for k in range(M):
                tmp.append((j,i+k))
            idx.append(tuple(tmp))

    honey_tmp = 0  # 꿀 채취 시 최대값
    result = 0
    comb(0, 0)
    print('#{} {}'.format(tc, result))



