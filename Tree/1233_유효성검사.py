import sys
sys.stdin = open('1233.txt', 'r')


def check():
    status = ('+', '-', '*', '/')
    if V[1] not in status:
        return 0
    for i in range(2, len(V)):
        if V[i] in status and not V[L[i]] and not V[R[i]]:  # 말단 노드는 사칙연산이 될 수 없다.
            return 0
        elif V[i] in status and V[P[i]] not in status: # 사칙연산의 부모는 사칙연산이다.
            return 0
        elif V[i] not in status and V[P[i]] not in status: # 숫자의 부모는 언제나 사칙연산이다.
            return 0

    return 1

for tc in range(1, 11):

    N = int(input())
    V = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    P = [0] * (N+1)
    for _ in range(N):
        tmp = input().split()
        V[int(tmp[0])] = tmp[1]
        if len(tmp) == 3:
            L[int(tmp[0])] = int(tmp[2])
            P[int(tmp[2])] = int(tmp[0])
        elif len(tmp) == 4:
            L[int(tmp[0])] = int(tmp[2])
            P[int(tmp[2])] = int(tmp[0])
            R[int(tmp[0])] = int(tmp[3])
            P[int(tmp[3])] = int(tmp[0])

    print('#{} {}'.format(tc, check()))