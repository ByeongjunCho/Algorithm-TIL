def to_decimal(arr, key):
    length = len(arr)
    dec = 0
    for i in range(length-1, -1, -1):
        dec += arr[i] * key ** (length-1-i)

    return dec

def money(two, thr):
    for i in range(1, len(two)):
        # 2진수 자리수 변화 0 or 1
        two[i] = not two[i]
        # 3진수 자리수 변화
        for j in range(len(thr)):
            thr_ori = thr[j]
            for k in [0, 1, 2]:
                if j and thr_ori != k:
                    thr[j] = k
                elif not j and k and thr_ori != k:
                    thr[j] = k
                else:
                    continue
                a = to_decimal(two, 2)
                b = to_decimal(thr, 3)
                if a == b:
                    return a
            # 3진수를 원본값으로 변환
            thr[j] = thr_ori
        # 2진수 자리값을 원본으로 변환
        two[i] = not two[i]



T = int(input())
for tc in range(1, T+1):
    two = list(map(int, list(input())))
    thr = list(map(int, list(input())))

    print('#{} {}'.format(tc, money(two, thr)))



