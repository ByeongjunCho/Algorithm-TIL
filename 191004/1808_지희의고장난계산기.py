def check(num):  # 숫자를 만들 수 있는지 확인
    while num > 0:
        num, k = divmod(num, 10)
        if k not in used:
            return False
    return True

def num_len(num):
    k = 0
    while num > 0:
        k += 1
        num //= 10
    return k

def calc(num):
    a, b = num, 0
    tmp = []
    while a > 0:
        for i in range(int(a**(0.5)), 1, -1):
            a, b = divmod(num, i)
            if b == 0 and check(i) and check(a):
                tmp.append(i)
                tmp.append(a)
                return tmp
            elif b == 0 and check(i):
                tmp.append(i)
    if b:
        return -1
    else:
        lenth = 0
        for s in tmp:
            lenth += num_len(s)
        return len(tmp) + lenth

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    N = int(input())
    # 사용할 수 있는 숫자를 구한다
    used = []
    for i in range(len(arr)):
        if arr[i] == '1':
            used.append(i)

    print('#{} {}'.format(tc, calc(N)))