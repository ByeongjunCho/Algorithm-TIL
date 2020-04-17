# 1493. 수의 새로운 연산
N = 300
source = [0] * (N+1)
source[0] = 0
source[1] = 1
for i in range(2, N+1):
    source[i] = source[i-1] + i-1

def get_xy(n):  # 좌표 반환
    for i in range(len(source)):
        if source[i] > n:
            tmp = i-1
            break
    k = tmp - (n - source[tmp])
    return tmp+1-k, k

def get_val(xy):
    idx = xy[0]+xy[1]-1
    return source[idx] + idx - xy[1]


T = int(input())
for tc in range(1, T+1):
    u, v = map(int, input().split())
    tmp_u = get_xy(u)
    tmp_v = get_xy(v)

    print('#{} {}'.format(tc, get_val([tmp_u[0] + tmp_v[0], tmp_u[1] + tmp_v[1]])))
