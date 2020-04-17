T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus = {x: 0 for x in range(5001)}
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus[i] += 1
    result = []
    P = int(input())
    for _ in range(P):
        C = int(input())
        result.append(str(bus[C]))
    print('#{} {}'.format(tc, ' '.join(result)))