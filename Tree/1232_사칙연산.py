c = []
status = ['+', '-', '*', '/']
def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        return a / b

def postorder(v):
    if v == 0:
        return
    postorder(L[v])
    postorder(R[v])
    if V[v] in status:
        b = c.pop()  # 피연산
        a = c.pop()  # 연산
        c.append(calc(a, b, V[v]))
    else:
        c.append(int(V[v]))
    return c[-1]

for tc in range(1, 11):

    N = int(input())
    V = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    for _ in range(N):
        tmp = input().split()
        V[int(tmp[0])] = tmp[1]
        if len(tmp) == 3:
            L[int(tmp[0])] = int(tmp[2])
        elif len(tmp) == 4:
            L[int(tmp[0])] = int(tmp[2])
            R[int(tmp[0])] = int(tmp[3])
    print('#{} {}'.format(tc, int(postorder(1))))