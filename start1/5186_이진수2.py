def under(n):
    # 점을 찾음
    for i in range(len(n)):
        if n[i] == '.':
            start = i
            break
    for i in range(start+1, len(n)):
        if n[i] != '0':
            return False
    return True

def tobin(n):
    times = 0
    while True:
        n *= 2
        times += 1
        if under(str(n)):
            break
        if times > 12:
            return 'overflow'
    result = bin(int(n))[2:]
    return '0'*(times - len(result)) + result

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print('#{} {}'.format(tc, tobin(N)))
